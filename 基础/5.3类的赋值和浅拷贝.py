#类对象的赋值操作
class Person:
    pass

p1=Person()
p2=p1

print(id(p1)) #14442544
print(id(p2)) #14442544 所以p1p2 本质上还是同一个对象
#变量浅拷贝 python 拷贝一般都是浅拷贝，拷贝时， 对象包含的子对象内容不拷贝，因为源对象和拷贝对象会引用同一个子对象
class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk


cpu1=CPU()
disk1=Disk()
computer1=Computer(cpu1,disk1)
import copy
computer2=copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk) #<__main__.Computer object at 0x012D4050> <__main__.CPU object at 0x0127F4B0> <__main__.Disk object at 0x012D4070>
print(computer2,computer2.cpu,computer2.disk) #<__main__.Computer object at 0x012D4050> <__main__.CPU object at 0x0127F4B0> <__main__.Disk object at 0x012D4070>
print("可以发现，二者之间除了主类内存地址不一样。但是子对象的没有拷贝走。就是用的同一个")

#变量深拷贝
computer3=copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.disk) #<__main__.Computer object at 0x012D4050> <__main__.CPU object at 0x0127F4B0> <__main__.Disk object at 0x012D4070>
print(computer3,computer3.cpu,computer3.disk) #<__main__.Computer object at 0x012D4050> <__main__.CPU object at 0x0127F4B0> <__main__.Disk object at 0x012D4070>
print("可以发现，二者之间内存地址全部不一样")
