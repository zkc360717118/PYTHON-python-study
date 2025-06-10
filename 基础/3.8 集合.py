#集合和列表和字典一样是可变序列，集合是没有value的字典

print("创建方式1")
#集合是没有value的字典,
s={1,2,3,3,2} #会去重
print(s)

print("创建方式2")
S2=set([1,2,3])
print(S2)

S3=set(range(6)) #也就是把集合转成元组
print(S3)

S4=set({124,4,4,5}) #这里会去重，也就是把元组转成set
print(S4)

#集合元素可以使用in  not in 进行判断操作
print("in 或者 not in 判断元素是否在集合中存在")
print(4 in S4)

#集合元素的增加操作
S4.add(1) #新增第一种方式
S4.update({7}) #新增的第二种的方式，用update 传参给集合
print(S4)

S4.update({9,10}) #新增的第二种的方式，用update 传参给集合
S4.update([11,12]) #新增的第二种的方式，用update 传参给list
S4.update((13,14)) #新增的第二种的方式，用update 传参给元组
print(S4)

print("######################集合的删除###############################")
testSet={1,2,3}
testSet.remove(2) #移除元素

testSet.pop()  #任意删除一个
# testSet.clear()  #清空集合中的元素
print(testSet)

print("################################集合之间的关系#####################33333")
s1={1,2,3,4}
s2={4,3,2,1}
print("二个集合是否相等,是看元素是否相同，和顺序没关系")
print(s1==s2) #True

print("一个集合是否是另一个集合的子集")
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
s4={10,20,30,40,50,60}

print(s2.issubset(s1)) #True
print(s3.issubset(s1)) #False

print("一个集合是否是另一个集合的超集")
print(s1.issuperset(s2)) #True
print(s2.issuperset(s3)) #False

print("二个集合集合是否是另一个集合的交集")
print(s1.isdisjoint(s2)) #二个集合之间有交集 ,返回false
print(s1.isdisjoint(s3))  #二集合之间有交集, 返回false
print(s1.isdisjoint(s4))  #二集合之间有交集 返回false
s6={9}
print(s2.isdisjoint(s6)) #没有交集，返回True

##################集合的数学操作#######################
print("交集")
s1={1,2,3,4}
s2={4,5,6,7}

print(s1.intersection(s2)) #求交集方式1 返回4
print(s1 & s2) #求交集方式2 返回4

print(s1 | s2) #并集操作1  {1, 2, 3, 4, 5, 6, 7}
print(s1.union(s2))  #并集操作2 {1, 2, 3, 4, 5, 6, 7}

print(s1.difference(s2)) #差集操作1 返回{1，2，3 }

print(s1.symmetric_difference(s2))#对称差集 {1, 2, 3, 5, 6, 7}


#集合生成式

newSet={i*i for i in range(1,101)}
print(newSet)
