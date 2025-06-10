square_generator = (x*x for x in range(10))
# print(next(square_generator)) #0
# print(next(square_generator)) #1

for v in square_generator:
    print(v)
    #的结果就是  0 1 4 9 16 25 36 49 64 81

#用生成器求斐波拉契
def  fib(limit):
    n,a,b=0,0,1
    while n < limit:
        yield b #惰性求值，开始迭代的时候才生成值，避免一次性加载所有数据到内存
        a,b = b,a+b
        n +=1
    return 'done'
f = fib(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))