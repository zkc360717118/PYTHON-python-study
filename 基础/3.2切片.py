li = list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li)
#切片是生成一个新的数组，原有的不发生变化
#切片[start:end:steps] >= start  和  < end
print(li[2:5]) #[3,4,5]
print(li[:4]) #[0,1,2,3]
print(li[5::]) #[6,7,8,9]
print(li[0:10:3]) #[0,3,6,9]

#负数怎么处理
print(li[5:-2]) #[5, 6, 7]
print(li[9:0:-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1]
print(li[9::-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1,0]
print(li[::-2]) #[9, 7, 5, 3, 1]

#切片快速的反转数组
reverse_li  = li[::-1]
print(reverse_li)