# calendar模块用来显示日历

import calendar

# 设置每周的起始日期。周一到周日分别对应0~6
print(calendar.setfirstweekday(calendar.SUNDAY))

# 返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0，即星期一 。
print(calendar.firstweekday())



c= calendar.calendar(2021)         #生成2021年的日历，并且以周日为其实日期吗
print(c)            #打印2021年日历



print(calendar.isleap(2021))      #True   闰年返回True，否则返回False


count= calendar.leapdays(1996,2021)
print(count)

print(calendar.month(2021, 3))
