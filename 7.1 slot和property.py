import traceback
from types import MethodType
#
# class MyClass(object):
#     pass
#
# def set_name(self,name):
#     self.name=name
#
# cls = MyClass()
# cls.name="kevin"
# print(cls.name)
#
# cls.set_name = MethodType(set_name,cls)
# cls.set_name("lara")
# print(cls.name)


#第二部分：可以看到上面的类可以被随便添加方法和属性，那么怎么实现只能添加指定的属性和方法？用魔术__slot__
class MyClass2(object):
    __slots__ = ['name1','set_name1']

def set_name(self,name):
    self.name=name

# cls = MyClass2()
# cls.name="kevin"
# print(cls.name)
#
# try:
#     cls.set_name = MethodType(set_name,cls)  #报错 AttributeError
# except AttributeError:
#     traceback.print_exc()

#第三部分，如果继承了第二部分的类，那么slots就不起作用
class ExtMyClass(MyClass2):
    pass

# ext_cls = ExtMyClass()
# ext_cls.age=20
#
# print(ext_cls.age)

#第四部分：使用@property实现get 和 set方法
class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise  ValueError("not int")
        elif (value<0) or (value>100):
            raise ValueError("not between 0 and 100")
        self._score = value

    #只读属性，就是不要设置setter 就行
    @property
    def double_socre(self):
        return self._score*2

# s = Student()
# s.score=100
# print(s.score) # 100
# print(s.double_socre) # 200

#第五部分：用描述器模拟生成property功能
