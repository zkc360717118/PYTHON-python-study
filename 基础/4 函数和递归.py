def func_name(p1,p2=100):
    print(p1,p2)
    return p1,p2

# r = func_name(1,2)
# print(type(r))

#可以指定参数名,从而可以乱序传入，但是不影响结果，不会报错
print(func_name(p2=100,p1=1))


#可变参数1
def func2(a,*b):
    print(type(b))

func2('a',1,2,3,4)

#可变参数  **可以接受kv类型的参数，这样获取的时候可以通过key来获取
def func3(a,**b):
    print(type(b))
    print(b['name'])

func3('a',name="kevin",gender="male")

#可变参数
def func4(a,*,china,world):
    print(china,world)

func4('a',china="中国",world='世界')

#可变参数
def func5(a,b,c=0,*args,**kv):
    print(a,b,c)
    print(args)
    print(kv)

func5(1,2)
func5(1,2,3)
func5(1,2,3,'a','b','c')
func5(1,2,3,'a','b',china="china",world="earth")

#把函数作为一个参数
def paraFunc(x,y):
    if x>y:
        return "x bigger"
    elif x==y:
        return "x equal y"
    else:
        return "y is bigger"

def funcPara(x,y,cp=None):
    if not cp:
        if x > y:
            return 1
        elif x==y:
            return 0
        else:
            return -1
    else:
        return cp(x,y)

print(funcPara(2,1,paraFunc))

#递归 写斐波拉契
# def fib(n):
#     if n < 1:
#         raise NameError
#     elif n <= 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(5))
# print(fib(6))
# print(fib(10))