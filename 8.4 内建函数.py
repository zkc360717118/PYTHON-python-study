#对一个列表或者数组 既要遍历索引又要遍历元素时
Li = [1,2,3]
for i in range(len(Li)):
    print(i,Li[i])


#使用enumerate将数据或者列表组成一个索引序列。使获取索引和值更加方便
for index,value in enumerate(Li):
    print(index,value)
