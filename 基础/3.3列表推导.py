#列表推导
li = [0]*10  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(li)
#生成20以内的偶数
li2 = [i * 2 for i in range(10)]
print(li2) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#生成二维数组 浅拷贝
li_2d = [[0]*3] * 3 #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(li_2d)
li_2d[0][0] = 100
print(li_2d) #浅拷贝 导致结果： [[100, 0, 0], [100, 0, 0], [100, 0, 0]]

#生成二维数组 深拷贝
li2_2d = [[0]*3 for i in range(3)]
print(li2_2d)
li2_2d[0][0] = 100
print(li2_2d) #[[100, 0, 0], [0, 0, 0], [0, 0, 0]]

s = {x for x in range(10) if x%2==0}
print(type(s)) # set
print(s) #{0, 2, 4, 6, 8}

s2 = (x for x in range(10))
print(type(s2)) #<class 'generator'>
for i in s2:
    print(i)

s3 = {x:x%2==0 for x in range(6)}
print(type(s3)) # <class 'dict'>
print(s3) # {0: True, 1: False, 2: True, 3: False, 4: True, 5: False}
