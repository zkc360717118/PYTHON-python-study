print("########################查询操作###############################")
str1="hello,hello"
print(str1.index("lo")) #3
print(str1.find("lo")) #3
print(str1.rindex("lo")) #9
print(str1.rfind("lo")) #9

# print(str1.index("lara")) #找不到报错 valueError
print(str1.find("lara")) #找不到返回-1

print("########################大小写操作###############################")
print(str1.upper()) #转换以后，会变成一个新的字符串，所以是一个新的内存地址
print(str1.lower())  #转换以后，会变成一个新的字符串，所以是一个新的内存地址
print(str1.swapcase())  #大写变小写， 小写变大写
print(str1.capitalize())
print(str1.title()) #每一个单词的i一个字符变成大写，剩下的变成小写
print("########################内容对齐操作###############################")
s='hello,Python'
print(s.center(20,"@")) #按照宽度20居中输出 “@@@@hello,Python@@@@”，二边用@填充
print(s.ljust(20,"@")) #按照宽度20靠左输出“hello,Python@@@@@@@@”，二边用@填充
print(s.ljust(10,)) #按照宽度10的宽度输出，但是本身s就已超出宽度10，这个时候就是原样输出。而不会裁剪
print(s.rjust(20,"@")) #按照宽度20靠右边输出“@@@@@@@@hello,Python”，二边用@填充
print(s.zfill(20)) #按照宽度20靠右边对其输出“00000000hello,Python”，左边用0填充

print("########################劈分操作###############################")
S="HELLO WORLD"
print(S.split()) #默认是空格来作为分割符号

s2="a!b!c!" #['HELLO', 'WORLD']
print(s2.split("!")) #['a', 'b', 'c', '']
print(s2.split("!",maxsplit=1))  #按照！来切分，但是只切分1次. ['a', 'b!c!']

print(s2.rsplit("!")) #['a', 'b', 'c', '']
print(s2.rsplit("!",maxsplit=1))  #按照！来切分，但是只切分1次. ['a!b!c', '']

print("########################判断操作###############################")
s1=""
print(s.isidentifier()) #判断字符串是否是合法的标识符  合法标识符 是字母数字下划线
print(s.isspace()) #是否是有空白字符串组成（回车，换行，水平制表符）
print(s.isalpha()) #是否全部由字母组成
print(s.isdecimal()) #判断是否全部是十进制的数字组成
print(s.isnumeric()) #是否是全部由数字组成
print(s.isalnum()) #全部由数字和字母组成

print("########################替换与合并操作###############################")
s2="hello,python.python.python"
print(s2.replace("python","java")) # hello,java.java.java
print(s2.replace("python","java",2)) #hello,java.java.python  只替换2次

lstr=["A","b","c"]
print("!".join(lstr)) #A!b!c

print("########################比较操作###############################")
print("abc" > "ab") # true 因为线比较第一位 发现一样，接着比较下一位，有一样，最后比较发现左边多了C  那就赢了
print("abc">"dec") # False 因为这里比较原理是： unicode value(编码值)， 调用内置函数ord可以 得到指定字符的编码值. 与内置函数ord 对应的是内置函数chr, 调用内置函数chr时候指定编码值 可以得到其对应的字符。
print(ord("a"),ord("d")) # 97 100 所以为什么上面a=87 d=100 当比较第一个位置的时候87>100 肯定是false
print(chr(97),chr(100)) # a  d

print("########################切片操作###############################")
#[start:end:steps]  和list 一样
str="hello,python"
print(str[:5])
print(str[6:])
print(str[::-1]) #倒置字符串 nohtyp,olleh
print(str[1:5:1]) #ello

print("########################格式化操作###############################")

name="kevin"
age=3
print("我%s,今年%d岁" % (name,age)) #"格式化第一种"
print("我{},今年{}岁".format(name,age)) #"格式化第二种"
print(f"我{name},今年{age}岁") #"格式化第三种"
print("%10d" % 99) #这里的10是整个的宽度。 这里返回“        99”
print("%10.3f" % 3.1514926) #这里的10是整个的宽度,小数点后保留3位。 这里返回“     3.151”
print("今年{:10.3f}岁".format(3.1514926)) #"今年     3.151岁"
print("今年{:.3f}岁".format(3.1514926)) #"今年3.151岁"

print("########################编码和解码###############################")
s="天要亡我啊" #5个汉字
gbk=s.encode(encoding="GBK")
utf=s.encode(encoding="UTF-8")
print(gbk) #  b'\xcc\xec\xd2\xaa\xcd\xf6\xce\xd2\xb0\xa1'   GBK 一个汉字占用2个字节, 所以这里有10个字节
print(utf)# b'\xe5\xa4\xa9\xe8\xa6\x81\xe4\xba\xa1\xe6\x88\x91\xe5\x95\x8a' utf-8一个汉字占用3个字节，所以有15个字节

print(gbk.decode(encoding="gbk")) #天要亡我啊