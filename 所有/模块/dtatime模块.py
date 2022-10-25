#datetime模块主要用来显示日期时间，这里主要涉及 date 类，用来显示日期； time 类，用来显示时间；
# datetime 类，用来显示日期时间；  timedelta类用来计算时间

import datetime as dt

#以一个下划线 _ 开始    _x
#以两个下划线 __ 开始  __x
#以两个下划线开始，在以两个下划线结束  __x__


#涉及到四个datetime/date/time/timedelta

#内置类
#list   tuple    int  str


print(dt.datetime.now())


#创建一个日期
print(dt.date(2020, 1, 1))

#创建一个时间
print(dt.time(18, 23, 45))

#获取当前的日期时间
print(dt.datetime.now())

#计算三天以后的日期时间
print(dt.datetime.now() + dt.timedelta(3))