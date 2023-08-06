# 查找某个目录下的目标文件
import os  # 引入操作系统模块
import sys  # 用于标准输入输出


def search(path, name):
    for root, dirs, files in os.walk(path):  # path 为根目录
        if name in dirs or name in files:
            flag = 1  # 判断是否找到文件
            root = str(root)+'\\'+name
            return root
            dirs = str(dirs)
            # return os.path.join(root, dirs)
    return -1


# path = input('请输入您要查找哪个盘中的文件（如：D:\\\）')
# print('请输入您要查找的文件名：')
# name = sys.stdin.readline().rstrip()  # 标准输入,其中rstrip()函数把字符串结尾的空白和回车删除
if __name__ == '__main__':
    path=r"C:\Users\RD\Desktop\U盘中金底稿目录-法律部分底稿-201905200"+'\\'
    name='1、走访照片'
    answer = search(path, name)
    if answer == -1:
        print("查无此文件")
    else:
        print(answer)