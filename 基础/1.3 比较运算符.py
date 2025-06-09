# life is hard ,but i am a tough man.

# 基础的> < <= >= == !=  很简单
#需要注意，这里比较的是值。。。不是标识, 如果要比较标识 就用is 或者is not

#但是要如果要对比对象引用呢？
a=10
b=10

print(a==b) #true
print(a is b) #true

#另外一个反例
print("#另外一个反例2")

list1=[1,2,3]
list2=[1,2,3]

print(list1 == list2) #True
print(list1 is list2) #False

#另外一个反例
print("#另外一个反例2")
list1=[1,2,6,7]
list2=[1,2,3]

print(list1 != list2) #false 比较的值
print(list1 is not list2) #true 比较的对象标识


