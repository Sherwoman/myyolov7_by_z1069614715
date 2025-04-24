import torch
import torch.nn as nn
import torch.nn.functional as F

class SEBlock(nn.Module):
    def __init__(self, in_channels, reduction_ratio=4):
        super(SEBlock, self).__init__()
        self.fc1 = nn.Linear(in_channels, in_channels // reduction_ratio, bias=False)
        self.fc2 = nn.Linear(in_channels // reduction_ratio, in_channels, bias=False)

    def forward(self, x):
        b, c, _, _ = x.size()
        y = F.adaptive_avg_pool2d(x, 1).view(b, c)
        y = F.relu(self.fc1(x))
        y = torch.sigmoid(self.fc2(y)).view(b, c, 1, 1)
        return x * y

class AdaptiveInceptionDWConv2d(nn.Module):
    # in_channels：输入通道数
    # square_kernel_size：方形卷积核大小，默认值为3
    # band_kernel_size：带状卷积核大小，默认值为7
    # branch_ratio：分配给每个卷积分支的通道比例，默认值为0.125
    def __init__(self, in_channels, square_kernel_size=3, band_kernel_size=7,branch_ratio=0.125):
        #super().__init__()
        super(AdaptiveInceptionDWConv2d, self).__init__()
        self.gc = int(in_channels * branch_ratio)  # 每个卷积分支的通道数
        self.dwconv_hw = nn.Sequential(
            nn.Conv2d(self.gc, self.gc, kernel_size=square_kernel_size, padding=square_kernel_size // 2,
                      groups=self.gc),
            SEBlock(self.gc)
        )

        # 定义w方向的带状卷积分支，并添加SE模块
        self.dwconv_w = nn.Sequential(
            nn.Conv2d(self.gc, self.gc, kernel_size=(1, square_kernel_size), padding=(0, square_kernel_size // 2),
                      groups=self.gc),
            SEBlock(self.gc)
        )

        # 定义h方向的带状卷积分支，并添加SE模块
        self.dwconv_h = nn.Sequential(
            nn.Conv2d(self.gc, self.gc, kernel_size=(square_kernel_size, 1), padding=(square_kernel_size // 2, 0),
                      groups=self.gc),
            SEBlock(self.gc)
        )
        self.identity_channels = in_channels - 3 * self.gc
        self.fusion = nn.Conv2d(in_channels, in_channels, kernel_size=1, groups=1)

    def forward(self, x):
        x_id, x_hw, x_w, x_h = torch.split(x, [self.identity_channels, self.gc, self.gc, self.gc], dim=1)
        out_hw = self.dwconv_hw(x_hw)
        out_w = self.dwconv_w(x_w)
        out_h = self.dwconv_h(x_h)
        out = torch.cat((x_id, out_hw, out_w, out_h), dim=1)
        out = self.fusion(out)
        return out

if __name__ == '__main__':
    from common import CatSplit, AM
    test1 = AM(1024, 1024)
    test2 = CatSplit(1024,  512, 1024)
    in1 = torch.randn(1, 1024, 20, 20)
    in2 = torch.randn(1, 1024, 20, 20)
    in3 = torch.randn(1, 1024, 20, 20)
    out1 = test1(in1)
    out = test2((out1, in2))
    print(f"out.shape={out.shape}")
    # inp = torch.randn(1, 32, 64, 64)
    # model = AdaptiveInceptionDWConv2d(in_channels=32)
    # outp = model(inp)
    # print('输入大小', inp.size())
    # print('输出大小', outp.size())
    '''
s1.shape=torch.Size([1, 512, 20, 20])
s2.shape=torch.Size([1, 512, 20, 20])
out.shape=torch.Size([1, 512, 20, 20])
out.shape=torch.Size([1, 1024, 20, 20])
'''