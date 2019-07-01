print(type(123))
print(type(123.89))
print(type(123.))
print(type("dssd"))
print(type([1,2,3]))
print(type((2,'c',4)))
print(type(set(['a',3,4])))
print(type({'a':1, 'b':2}))

#字符串取出空格和特殊符号
print(" A   A".strip())
print("BB ".rstrip())
print("acc".lstrip('a'))

#查找字符串字符串
str1 = "abc"
str2 = "DabcD"
print(str2.index("abc"))  # 查看abc在str2中出现在什么位置

#比较字符串 直接比较，不用cmp函数
print(str1>str2)
print(not "")

#字符串长度
print(len(str1))

#大小写转换
print(str1.upper())
print(str1.lower())
print(str1.capitalize())

##字符串的分割与合并
str3 = """a
b
c"""
s = str3.split('\n')
d = str3.splitlines()
print(s)
print(d)
print("-".join(s))

#字符串常用判断
print(str3.startswith("S"))
print(str3.isalnum())
print("\tasd123".isalnum())
print(str3.isalpha())
print(str3.isdigit())
print(" ".isspace())
print("DSsD ".isupper())
print("asdf ".islower())
print("Abc ".istitle())

#数字和字符串之间的转化
print(str(3))
print(str(3.))
print(str(3.12))
print(str(-3.3))

print(int("3"))
print(float("3."))
print(float("3.3"))
#字符串和数组之间的转换
test="abc"
l = list(test)
print(l)

#None的判断
x = None
if  x is None:
    print("it is None")
elif x ==1:
    print("x = 1")
else:
    print("i am happy")

if not x:
    print("it is None")

#for 循环
for i in range(0,30,5):
    print(i)

#while 循环
s=0
i=1
while i <= 100:
    s+=i
    i+=1
print(s)
#continue中断当前循环，break跳出所有循环






