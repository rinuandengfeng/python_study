#time模块不仅可以用来显示时间，还可以控制程序，让程序暂停（使用sleep函数）

import time

print(time.time())        #获取从1970-01-01 00:00:00   UTC  到现在时间的秒数

print(time.strftime("%Y-%m-%d %H:%M:%S"))     #按照指定格式输出时间

print(time.asctime())   #Mon Apr 15 20:03:23  2019

print(time.ctime())    #Mon  Apr 15 20:03:23 2019

print('hello')
print(time.sleep(10))    #让线程暂停10秒钟
print('world')
