"""文件的编码格式
    1. python的解释器使用的unicode 内存
    2.py 文件在磁盘上使用的utf-8 存储 （外存）
    3. ASCII 128字符
        3.1 ISO8859-1 256 字符
            3.1.1 GB2312
                3.1.1.1 GBK
                    3.1.1.1 GB18030
            3.1.2 UTF-8  变长编码 英文一个字节 汉字3个字节. 是unicode 的实现
        3.2 UNICODE 定长编码 2个字节表示1个字符

"""

"""
文件对象的常用方法
1. read（【size】） 把文件的读取size个字节或者字符的内容返回。如果没有size ,默认读取所有
2.readline 读取一行
3.readlines 读取每一行，放到list.  每一行对应list的一个元素
4.write(str) 字符写入到文件
5.writeslines(s_list) 字符串列表写入到我呢见， 不添加换行符
6.seek(offset,[wherece]) 把文件指针移动到新的位置。 offset表示相对于wherece的位置。 offset 正数表示结束方向移动。 负数表示反方向移动。
    wherece 0表示从头开始计算 1 表示从当前位置开始计算 2从文件末尾开始计算
7. tell 返回文件指针的当前位置
8. flush 把缓冲区的内容写入到文件，但是不关闭文件
9. close 把缓冲去的内容写入文件，并关闭文件，释放文件的相关资源
"""

#文件读写 方法一
print("#文件读写 方法一 readlines 把内容一次性读到一个List中")
# file1 = open("./../file/test.txt")
# file2 = open("output.txt","w")
#
# while True:
#     line = file1.readline()
#     file2.write(line)
#     if not line:
#         break
# file1.close()
# file2.close()

#文件读写 方法二
print("#文件读写 方法二 for循环")

# file3 = open("output2.txt","w")
# for line in open("./../file/test.txt"):
#     #这里可以进行逻辑处理
#     file3.write(line)
# file3.close()

#文件读写第三种方法 with.open自带关闭文本
print("#文件读写 方法三 with.open")

# with open("./../file/test.txt","r") as f:
#     data = f.read()
#     print(data)
#
# with open("./../file/test.txt","r") as f:
#     for line in f:
#         print(line)

# with open("./../file/test.txt", "r") as f:
#     with open("output3.txt","w") as f2:
#         f2.write(f.read())

#二进制文件读取
# f = open("./../file/test.jpg",'rb')
# print(f.read())

#文件和目录的操作
import os
# print(os.name)
# print(os.getcwd()) #当前的目录
# print(os.listdir("../基础/"))
# print(os.path.abspath("./")) #绝对路径
# print(os.path.exists("/laaa.txt")) #路径是否存在
# print(os.path.splitext("/laaa.txt")) #分离文件名和扩展名 ('/laaa', '.txt')
# print(os.path.basename("./dd/laaa.txt")) #从一个路径中提取文件名 laaa.txt
# print(os.path.dirname("./dd/laaa.txt")) #从一个路径中提取文件路径，不包含文件名 ./dd
# print(os.path.isdir("../基础")) #是否是个文件夹

#课堂实例 列出指定目录下的所有py文件
import os
def listAllPyFiles(path):
    if(os.path.isdir(path)):
        for file in os.listdir(path):
            if(file.endswith(".py")):
                print(path+"/"+file)
            elif(os.path.isdir(path+"/"+file)):
                print(f"find dir,go deepper into {path}/{file}!!!!")
                listAllPyFiles(path+"/"+file)
            else:
                pass
                # print(f"this is not a python file {file}")
    else:
        print("it is not a directory")

listAllPyFiles("F:\projects\PYTHON-python-study")
