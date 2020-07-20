################List################
li = [1,2,'333',[43,4],{1:"one",2:"two"}]
print(type(list))
print(type(li))

#元素的访问
print(li[0])
print(li[1])
print(li[-1])

#查找元素的位置
print(li.index("333")) #2
# print(li.index("3阿帆")) #报错

#添加元素
a = list()
a.append(4)
a.append(["a","b"]) #这里会把数组当成一个元素加入到list
a.extend(["e1","e2"]) # 这里会把数组元素拆开，一个一个加进去
print(a)

#判断是否为空 和 none
if not a:
    print("empty")
if a is None:
    print("none")

#遍历数组
for i in a:
    print(i)

#删除元素
del(li[-1])

################Tuple################
t = (1,2,3,"asd")
print(type(t))

#元组不能修改元素，不能新增，是只读的容器
# t[0] = '4' #会报错
# t.append("d") # 会报错

#遍历同list一样

################字典dict################
d = {"a":1,"b":2,"c":3}  #无序的
#新增元素
d["dog"] = "金毛"

#修改元素
d["dog"] ="二哈"

#访问元素
print(d["a"])

#判断key是否存在
print("a" in d) # true
print(3 in d) #false

#删除元素
del(d["a"])

#遍 历
for key in d:
    print(d[key])
for k,v in d.items():
    print(k,v)
################set################
s_a = set([1,2,2,3,4,5])
s_b = set([4,5,6,7,8,9])
print(s_a)
print(s_b)

#判断 元素是否存在
print(3 in s_a)
#并集
print(s_a | s_b)
print(s_a.union(s_b))
#交集
print(s_a.intersection(s_b))
#差集
print(s_a - s_b)
print(s_a.difference(s_b))
#对称差（A|B) - (A&B)
print(s_a ^ s_b)
print(s_a.symmetric_difference(s_b))
#新增一个元素
s_a.add('x')
#新增多个
s_a.update([4,5,60,70])
print(s_a)
#删除某个元素
s_a.remove(70)
#遍历
for v in s_a:
    print(v)
for v in iter(s_a):
    print(v)