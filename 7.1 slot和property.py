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

#第五部分：用描述器模拟生成property功能(不想学，下次再说)

#第六部分 类的默认行为与定制
class defaultAction:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "hello "+self.name

# t = defaultAction("bitch")  #如果没有__str__重写，就是标准的输出  否则就是自定义的hello bitch
# print(t)

#把类做成迭代器实现 斐波拉契
class Fib100:
    def __init__(self):
        self._1,self._2 = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self._1,self._2 =self._2,self._2+self._1
        if self._1 > 100:
            raise  StopIteration
        return self._1

# for i in Fib100():
#     print(i)

# 实现下标访问 需要重写__getitem__选项
class Fib2:
    def __getitem__(self, n):
        a,b = 1,1
        for i in range(n):
            a,b = b, a+b
        return a
# f = Fib2()
# # print(f[1])
# # print(f[5])
# # print(f[10])

#第七部分  枚举
from enum import Enum

Month = Enum("Month",('Jan','Feb','Mar','Apr'))
# print(Month) #<enum 'Month'>
# print(Month.__members__.items()) ('Jan','Feb','Mar','Apr')
# for name , member in  Month.__members__.items():
#     print(name,"=>",member,',',member.value)
# print(Month.Jan) # Month.Jan

#第八部分 元类 元编程
def init(self,name):
    self.name = name

def say_hello(self):
    print('Hello! %s!' % self.name)


Hello = type('Hello',(object,),dict(__init__ = init,hello=say_hello)) #这里等同于创建了一个类，然后有初始化方法 和 hello方法
# h = Hello("name")
# h.hello() #Hello! name!


#第九部分 元类（控制类的创建）
class ListMetaClass(type):  #元类一定要继承自type
    def __new__(cls,name,bases,attrs):
        # print(cls)
        # print(name)
        # print(bases)
        # print(type(attrs))
        attrs['add'] = lambda self,value: self.append(value)
        return type.__new__(cls,name,bases,attrs)

    #新建一个类指定继承自list，然后指定元类是ListMetaClass， 在上面元类中
    #通过__new__新建一个一个add方法，方法体通过lambda方式实现了
class  MyList(list,metaclass=ListMetaClass):
    pass


# mli = MyList()
# mli.add(1)
# mli.add(2)
# mli.add(3)
# print(mli)

#第十部分 ORM框架实例实现
    #背景：假如我们要自己写model,怎么保证save方法能获取到继承类User的id，name，然后保存呢？
# class User(Model): #都是伪代码
#     id = IntegerField('id')
#     name = StringField('name')
#
# u = User()
# u.id =100
# u.name = 'tome'
# u.save()

    #用元类解决上面的问题
class Field:
    def __init__(self, name, col_type):
        self.name = name
        self.col_type = col_type

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'integer')

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(1024)')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Model name: %s' % name)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Field name: %s' % k)
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kvs):
        super(Model, self).__init__(**kvs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'." % key)

    def __setattr__(self, key, value):
        print('__setattr__')
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('sql:', sql)
        print('args:', args)

class User(Model):
    id = IntegerField('id')
    name = StringField('name')

# u = User(id = 100, name = 'Tom')
# u = User()
# u.id = 100
# u.name = 'Tom'
# u.save()



#第十一部分：测试
import unittest
class MyDict(dict):
    pass

class TestMyDict(unittest.TestCase):
    def setUp(self):
        print("测试前")

    def tearDown(self):
        print("测试后清理")
    def test_init(self):
        md = MyDict(one = 1,two=2)
        self.assertEqual(md['one'],1)
        self.assertEqual(md['two'],2)

# if __name__ == '__main__':
#     unittest.main()

#第十一部分：日志
import logging

logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')