#什么是元组

#元组的创建
print("元组 没有增删改")
print("第一种方式")
T1=(1,2,3) #直接创建

print("第二种方式")
T1_1=1,2,3 #第一种方式的省略方式，

print("第三种方式")
T2=tuple([1,2,3]) #用内置函数

print("如果只有一个元素的元组，要额外多加一个逗号，不然会当成string或者数字")
T_special=("lara")
print(type(T_special))
T_special_FIX=("lara",)
print(type(T_special_FIX))

#元组的遍历
for i in T1:
    print(i)
