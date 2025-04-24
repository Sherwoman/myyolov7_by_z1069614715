import os

def is_allfish(folder_path, name_as_fish):
    # 遍历文件夹中的所有txt文件
    sum = [0,0,0,0]
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    values = line.split()
                    #file.write(' '.join(values) + '\n')
                    if values:
                        if values[0]!='0':
                            print(filename)
                            if name_as_fish:
                                values[0] = '0'
                        sum[int(values[0])]+=1

    return sum

def count(folder_path):
    list = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
    # 遍历文件夹中的所有txt文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            seventh_char = filename[6] if len(filename) > 6 else None
            tw_char = filename[19] if len(filename) > 20 else None

            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if "canthopagrus_palmaris" in filename:  # Acanthopagrus_palmaris 859
                        list[0] += 1
                    if "mniataba_caudivittatus" in filename:  # Amniataba_caudivittatus 50
                        list[1] += 1
                    if "aranx" in filename:  # Caranx_sexfasciatus_juvenile/Caranx 3060
                        list[2] += 1
                    if "pinephelus" in filename:  # Epinephelus 49
                        list[3] += 1
                    if "erres" in filename:  # Gerres 239
                        list[4] += 1
                    if "utjanus" in filename:  # Lutjanus_russellii_EJP 20
                        list[5] += 1
                    if "_F1_" in filename:  # F1 7702
                        list[6] += 1
                    if "_F2_" in filename:  # F2 1794
                        list[7] += 1
                    if "_F3_" in filename:  # F3 291
                        list[8] += 1
                    if "_F4_" in filename:  # F4 438
                        list[9] += 1
                    if "_F5_" in filename:  # F5 127
                        list[10] += 1
                    if "_F6_" in filename:  # F6 358
                        list[11] += 1
                    if "_F7_" in filename:  # F7 177
                        list[12] += 1
                    if "_no_fish_" or "_NF" in filename:  # empty
                        list[13] += 1
    sum = list[0] + list[1] + list[2] + list[3] + list[4] + \
          list[5] + list[6] + list[7] + list[8] + list[9] + \
          list[10] + list[11] + list[12] + list[13] + list[14]

    print("所有文件已处理完成。")
    print(f"SUM                         :{sum}")
    print(f"Acanthopagrus_palmaris      ={list[0]}")
    print(f"Amniataba_caudivittatus     ={list[1]}")
    print(f"Caranx_sexfasciatus_juvenile={list[2]}")
    print(f"Epinephelus                 ={list[3]}")
    print(f"Gerres                      ={list[4]}")
    print(f"Lutjanus_russellii_EJP      ={list[5]}")
    print(f"F1                          ={list[6]}")
    print(f"F2                          ={list[7]}")
    print(f"F3                          ={list[8]}")
    print(f"F4                          ={list[9]}")
    print(f"F5                          ={list[10]}")
    print(f"F6                          ={list[11]}")
    print(f"F7                          ={list[12]}")
    print(f"No                          ={list[13]}")

def rewrite(folder_path):
    list = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0]
    # 遍历文件夹中的所有txt文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            file_number = 0

            # 打开并读取文件
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # 打开文件准备修改（可以选择覆盖原文件或者另存新文件）
            with open(file_path, 'w') as file:
                for line in lines:
                    if "canthopagrus_palmaris" in filename:  # Acanthopagrus_palmaris 859
                        file_number = 0
                    #if seventh_char == "c" and tw_char == "a":  # acanthopagrus_and_caranx 299
                    #    file_number = 'test'
                    if "mniataba_caudivittatus" in filename:  # Amniataba_caudivittatus 50
                        file_number = 1
                    if "aranx" in filename:  # Caranx_sexfasciatus_juvenile/Caranx 3060
                        file_number = 2
                    if "pinephelus" in filename:  # Epinephelus 49
                        file_number = 3
                    if "Gerres" in filename:  # Gerres 239
                        file_number = 4
                    if "utjanus" in filename:  # Lutjanus_russellii_EJP 20
                        file_number = 5
                    if "_F1_" in filename:  # F1 7702
                        file_number = 6
                    if "_F2_" in filename:  # F2 1794
                        file_number = 7
                    if "_F3_" in filename:  # F3 291
                        file_number = 8
                    if "_F4_" in filename:  # F4 438
                        file_number = 9
                    if "_F5_" in filename:  # F5 127
                        file_number = 10
                    if "_F6_" in filename:  # F6 358
                        file_number = 11
                    if "_F7_" in filename:  # F7 177
                        file_number = 12

                    list[file_number] += 1

                    values = line.split()
                    # 假设我们只修改每行第一个数值，将其加上file_number
                    if values:
                        values[0] = str(file_number)  # 转换为浮点数并加上文件名中的数字

                    # 将修改后的行写回文件
                    file.write(' '.join(values) + '\n')
                    print(values[0])

    sum = list[0] + list[1] + list[2] + list[3] + list[4] + \
          list[5] + list[6] + list[7] + list[8] + list[9] + \
          list[10] + list[11] + list[12]

    print("所有文件已处理完成。")
    print(f"SUM                         :{sum}")
    print(f"Acanthopagrus_palmaris      ={list[0]}")
    print(f"Amniataba_caudivittatus     ={list[1]}")
    print(f"Caranx_sexfasciatus_juvenile={list[2]}")
    print(f"Epinephelus                 ={list[3]}")
    print(f"Gerres                      ={list[4]}")
    print(f"Lutjanus_russellii_EJP      ={list[5]}")
    print(f"F1                          ={list[6]}")
    print(f"F2                          ={list[7]}")
    print(f"F3                          ={list[8]}")
    print(f"F4                          ={list[9]}")
    print(f"F5                          ={list[10]}")
    print(f"F6                          ={list[11]}")
    print(f"F7                          ={list[12]}")
"""
所有文件已处理完成。
SUM                         :15463
Acanthopagrus_palmaris      =1158
Amniataba_caudivittatus     =50
Caranx_sexfasciatus_juvenile=3060
Epinephelus                 =49
Gerres                      =239
Lutjanus_russellii_EJP      =20
F1                          =7702
F2                          =1794
F3                          =291
F4                          =438
F5                          =127
F6                          =358
F7                          =177
"""

def rename(folder_path):
    n = 6  # 目标文件名长度
    for idx, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith('.txt'):
            new_name = f"{str(idx//2+9964).zfill(n)}.txt"  # 使用格式化方法生成n位数字

            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)

            os.rename(old_file_path, new_file_path)
            print(f"文件 {filename} 重命名为 {new_name}")

        if filename.endswith('.jpg'):
            new_name = f"{str(idx//2+9964).zfill(n)}.jpg"  # 使用格式化方法生成n位数字

            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)

            os.rename(old_file_path, new_file_path)
            print(f"文件 {filename} 重命名为 {new_name}")
            if filename[6] == "c" and filename[19] == "a":
                print(new_name)


if __name__=='__main__':
    # 指定包含txt文件的文件夹路径
    folder_path = 'deepfish'  # 替换为你的文件夹路径
    list = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
    # rename(folder_path=folder_path)

    count(folder_path=folder_path)
    # rewrite(folder_path=folder_path)
    # temp = is_allfish(folder_path=folder_path, name_as_fish=False)
    # print(f"temp[0]={temp[0]}")
    # print(f"temp[1]={temp[1]}")
    # print(f"temp[2]={temp[2]}")
    # print(f"temp[3]={temp[3]}")
    # sum = list[0] + list[1] + list[2] + list[3] + list[4] + \
    #       list[5] + list[6] + list[7] + list[8] + list[9] + \
    #       list[10] + list[11] + list[12] + list[13] + list[14]
    #
    # print("所有文件已处理完成。")
    # print(f"SUM                         :{sum}")
    # print(f"Acanthopagrus_palmaris      ={list[0]}")
    # print(f"acanthopagrus_and_caranx    ={list[1]}")
    # print(f"Amniataba_caudivittatus     ={list[2]}")
    # print(f"Caranx_sexfasciatus_juvenile={list[3]}")
    # print(f"Epinephelus                 ={list[4]}")
    # print(f"Gerres                      ={list[5]}")
    # print(f"Lutjanus_russellii_EJP      ={list[6]}")
    # # print(f"Others                      ={list[7]}")
    # print(f"F1                          ={list[7]}")
    # print(f"F2                          ={list[8]}")
    # print(f"F3                          ={list[9]}")
    # print(f"F4                          ={list[10]}")
    # print(f"F5                          ={list[11]}")
    # print(f"F6                          ={list[12]}")
    # print(f"F7                          ={list[13]}")
    # print(f"No                          ={list[14]}")


'''
RESULTS:
SUM                         :30926
Acanthopagrus_palmaris      =859
acanthopagrus_and_caranx    =299 for test
Amniataba_caudivittatus     =50
Caranx_sexfasciatus_juvenile=3060
Epinephelus                 =49
Gerres                      =239
Lutjanus_russellii_EJP      =20
F1                          =7702
F2                          =1794
F3                          =291
F4                          =438
F5                          =127
F6                          =358
F7                          =177
No                          =15463
'''