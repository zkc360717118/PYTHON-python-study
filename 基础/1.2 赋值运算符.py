# life is hard ,but i am a tough man.
#1 支持链式赋值
print("#1 支持链式赋值")
a=b=c=20
#################下面3个对象都是指向同一个对象，所以是同一个内存地址
print(a,id(a)) #  id可以知道对象的唯一标识
print(b,id(b)) #  id可以知道对象的唯一标识
print(c,id(c)) #  id可以知道对象的唯一标识

#2 支持参数赋值 -+ *= -= /=
print("#2 支持参数赋值")
a+=30
print(a)

#3 支持系列解包赋值
print("#3 支持系列解包赋值")
a,b,c=20,30,40
print(a)
print(b)
print(c )

print("####一个有趣的事情，交换2个变量的值，在java中需要写好几行的代码，这里2行就搞定#####")
a,b=1,2
print("交换之前",a,b)
a,b=b,a
print("交换之后",a,b)
