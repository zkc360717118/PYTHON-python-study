class A:
    pass

class B:
    pass

class C(A,B):
    def __init__(self,name,age):
        self.age=age
        self.name=name


x=C("jack",10)
print(x.__dict__) #实例对象的属性字典
print(x.__class__) #实例对象的所属类
print(C.__bases__) #某个类的基类
print(C.__mro__) #某个类的层次机构

class D(A):
    pass

print(A.__subclasses__()) #返回父类A的子类列表


#################################__new__ 和 __init__ 的使用#############################
class Person(object):
    def __init__(self,name,age):
        print("Person init called, self 的id值为{0}".format(id(self)))
        self.name=name
        self.age=age

    def __new__(self,name,age):
        print("Person 被实例化之前, self的id值{0}".format(id(self)))
        obj=super().__new__(self)
        print("Person 被实例化之后, self的id值{0}".format(id(obj)))
        return obj

print("object 类对象的id是{0}".format(id(object)))
print("Person 类对象的id是{0}".format(id(Person)))

#创建person 对象
p=Person("jack",10)
print("p这个对象的实例对象id {0}".format(id(p)))
