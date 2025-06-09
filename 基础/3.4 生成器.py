square_generator = (x*x for x in range(10))
# print(next(square_generator)) #0
# print(next(square_generator)) #1

for v in square_generator:
    print(v)

#用生成器求斐波拉契
def  fib(limit):
    n,a,b=0,0,1
    while n < limit:
        yield b
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