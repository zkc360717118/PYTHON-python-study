class Foo:
    def bar(self):
        print("bar")

    def hello(self,name):
        print('i am %s' %name)

obj = Foo()
obj.hello("kevin")


class Foo2:
# 这里我们可以创建一个类级别的变量
# 它不会随着由此类创建的变量而变化
    name = "unchangekevin"
    def hello(self,name):
        print("this is unchange %s" %self.name);
        print("this is change name %s" %name)

obj2 = Foo2()
obj2.hello("kevin2")

#构造方法
class Foo3:
    def __init__(self):
        self.name="构造的变量"

    def hello(self,name):
        print("class variable: %s" %self.name)
        print("function variable: %s" %name)

obj3 = Foo3()
obj3.hello("方法变量")

#构造方法2 新建类的时候传入类的变量
class Foo4:
    def __init__(self,name1):
        self.name = name1

    def hello(self, name):
        print("class variable: %s" % self.name)
        print("function variable: %s" % name)

obj4 = Foo4("构造2变量")
obj4.hello("方法变量")

#私有变量
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def detail(self):
        print(self.__age)
        print(self.__name)
obj5 = Student("name","age")
obj5.detail()

#继承
class StudentFather:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def detail(self):
        print(self.name)
        print(self.age)

class primaryStudent(StudentFather):
    def lol(self):
        print("不符sala！")

class highSchool(Student):
    def gf(self):
        print("i hava girlfriend")

jc = primaryStudent("kevin","12")
jc.detail()
jc.lol()



#解释类中的“好猫类型”
class F1:
    pass
    # 假设，S1是我们的正统类，它继承于根正苗红的F1，是我们的正统

class S1(F1):
    def show(self):
        print('S1.show')

    # S2是路人甲，是个歪瓜裂枣，但是他自己也有一个叫show的方法。
class S2:
    def show(self):
        print('S2.show')
    # 在Java或C#中定义函数参数时，必须指定参数的类型，也即是说，我们如果用# Java写下面的Func，
    # 需要告知，obj是F1类还是其他什么东西。# 如果限定了F1，那么S2是不可以被采纳的。
    #  然而，在Python中，一切都是Obj，它不care你到底是什么类，直接塞进去就可以

    def Func(obj,T):
        obj.show()

# 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show
# s1_obj = S1()Func(s1_obj)
# 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show
s2_obj = S2()
S2().Func(s2_obj)


#判断类的类型，如何判断他们是不是同一种类型
print(type(s2_obj)) #<class '__main__.S2'>

type1 = S2()
type3 = type1
type2 = S2()
print(type1 == type2) # false
print(type1 == type3) # true
print(type("212") == str) #true

#对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir(type1))

print("22".__len__())
print(len("22"))


class MyObject:
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

act01 = MyObject()
print(hasattr(act01,'x'))#true
print(hasattr(act01,'y'))#false
setattr(act01,"y",19)
print(hasattr(act01,'y'))#true
print(getattr(act01,"y"))
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
hasattr(obj, 'power') # 有方法'power'吗？
getattr(obj, 'power') # 获取方法'power'

