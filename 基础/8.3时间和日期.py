# time模块
import time

print(time.time()) #1562203451.6068141
print(time.localtime()) #time.struct_time(tm_year=2019, tm_mon=7, tm_mday=4, tm_hour=9, tm_min=24, tm_sec=11, tm_wday=3, tm_yday=185, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))) #2025-06-11 23:04:05 格式化后的时间
for i in range(3):
    time.sleep(0.5)
    print("tik")

#datetime模块
import datetime

print("today is: ",datetime.date.today()) #today is:  2019-07-04
print("now is: ",datetime.datetime.now()) #now is:  2019-07-04 09:26:57.307291
print(datetime.date(2016,11,4)) # 2016-11-04
print(datetime.time(11,4)) # 11:04:00


#计算昨天你和今天的日期
import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday,today,tomorrow)

newTime=datetime.datetime.strptime("2016-11-1","%Y-%m-%d")#根据传进来的str  format 一个datetime
print(type(newTime))
