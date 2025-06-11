import sys
import time
import os #提供访问操作系统服务功能的标准库
import calendar #日期相关的函数标准库
import urllib #读取网上（服务器） 的数据标准库
import json #用于使用JSON 序列化和反序列化对象
import re #正则相关
import  math #算术运算相关的
import decimal #精确控制运算精度，有效数位和四舍五入操作的十进制运算
import logging #提供灵活的记录事件，错误，调试信息日志的功能


print(sys.getsizeof(24)) #使用了多少字节 结果是14
print(sys.getsizeof(45)) #使用了多少字节 结果是14
print(sys.getsizeof(True)) #使用了多少字节 结果是14
print(sys.getsizeof(False)) #使用了多少字节 结果是12

import time
print(time.time()) #1749624244.618841
print(time.localtime(time.time())) #time.struct_time(tm_year=2025, tm_mon=6, tm_mday=11, tm_hour=14, tm_min=44, tm_sec=4, tm_wday=2, tm_yday=162, tm_isdst=0)

