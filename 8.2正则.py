#正则2种模式匹配： 搜索search（） 和 匹配 match（）
import re

m = re.match(r'dog',"dog cat cow dogd")
print(m.group()) #dog   只从第一个单词开始匹配
print(m) #<_sre.SRE_Match object; span=(0, 3), match='dog'>
print(re.match(r"cat","dog cat dog")) #None

s = re.search(r'cat',"dog cat dog")
print(s.group) #<built-in method group of _sre.SRE_Match object at 0x00000000028F35E0>
print(re.findall(r'dog','dog cat dog')) #['dog', 'dog']


contactInfo = 'Doe,John:555-1212'
m = re.search(r'(\w+),(\w+):(\S+)',contactInfo)
print(m.group(0)) #Doe,John:555-1212   返回珍格格匹配到的字符
print(m.group(1)) #Doe
print(m.group(2)) #John
print(m.group(3)) #555-1212