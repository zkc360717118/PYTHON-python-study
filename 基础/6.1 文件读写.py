#文件读写 方法一
# file1 = open("file/test.txt")
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
# file3 = open("output2.txt","w")
# for line in open("file/test.txt"):
#     #这里可以进行逻辑处理
#     file3.write(line)
# file3.close()

#文件读写第三种方法 with.open自带关闭文本
# with open("file/test.txt","r") as f:
#     data = f.read()
#     print(data)
#
# with open("file/test.txt","r") as f:
#     for line in f:
#         print(line)

# with open("file/test.txt", "r") as f:
#     with open("output3.txt","w") as f2:
#         f2.write(f.read())

#二进制文件读取
# f = open("file/test.jpg",'rb')
# print(f.read())

#文件和目录的操作
import os
print(os.name)
