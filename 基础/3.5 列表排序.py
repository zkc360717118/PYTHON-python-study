list1=[2,4,6,1]
print(id(list1))

list1.sort(reverse=True) #降序排雷
print(list1,id(list1))  #用id 查看排序是否有新建一个list对象，和下面id 的值进行对比

list1.sort(reverse=False) #如果不写reverse=False 默认是False 升序排列
print(list1,id(list1))