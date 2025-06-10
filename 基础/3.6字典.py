#字典是什么
    # 和列表一样，是一个可变序列。以键值对的方式存储数据，字典是一个无序的序列
#字典的原理
    #key必须要是不可变的，因为key要序列化存储。
    #根据key的hash函数的值 去查找value所在的位置
#字典的创建 ， 以及获取,增加和删除元素
print("创建方式1")
dict1= {"zhangshan":1, "kevin":4,"lisi":4}
print(dict1)
print(type(dict1))

print("创建方式2")
dict2=dict(name='jack',age=44)
print(dict2)
print(type(dict2))

print("获取方式1")
print(dict2["name"])

print("获取方式2")
print(dict2.get("name"))

print("获取方式1和获取方式2的区别就是，如果查找的key不存在 ['KEY']获取的方式会包keyError, 但是get方式返回的是None，更友好")
# print(dict2["wangmazi"])
# print(dict2.get("wangmazi"))

print("判断字典是否包含某个key, 注意是包含key ,不是值")
print("kevin" in dict1)

print("删除字典的某个元素")
del dict1["zhangshan"]
print(dict1)

print("清空字典的所有元素")
# dict1.clear()
# print(dict1)

#字典视图操作
keys=dict1.keys()  #获取所有的key
print(keys)
print(type(keys))

values=dict1.values()  #获取所有的values
print(values)
print(type(values))

kvs=dict1.items()  #获取所有的key-value 键值对
print(kvs)
print(type(kvs))

#字典元素的遍历
for k,v in dict1.items():
    print(k,v)

for i in dict1:
    print(i,dict1.get(i))

#字典元素key 重复了，不会报错，但是会覆盖前者相同key的键值对
d={"name":"kevin","name":"lara"}
print(d)# 只会保留 {"name":"lara"}

#字典的推导式(生成式 ),用到ZIP内置function
items=["price","name","num"]
values=[10,"bike",3]

newDic={ label.upper():v for label,v in zip(items,values)}
print(newDic)
