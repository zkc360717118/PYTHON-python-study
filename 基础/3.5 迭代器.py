from collections import Iterable
from collections import Iterator

print(isinstance([1,2,3],Iterable)) #True
print(isinstance({},Iterable)) #TRUE
print(isinstance("2323",Iterable)) # TRUE
print(isinstance(3,Iterable)) #false


print(isinstance([1,2,3,],Iterator)) #false
g = (x *x for x in range(10))
print(type(g))  #<class 'generator'>
print(isinstance(g,Iterator)) #true
print(isinstance(g,Iterable)) #true


#用生成器重写斐波拉契

def fib(limit):
    n,a,b = 0, 0, 1
    while n<limit:
        yield b # 只有用了yield 这个fib函数才是迭代器,否则就只是可迭代对象
        a,b = b,a+b
        n += 1
    return "done"

f = fib(6)
print(type(f))
print(isinstance(f,Iterable)) #true
print(isinstance(f,Iterator)) #true
for  i in f:
    print(i)