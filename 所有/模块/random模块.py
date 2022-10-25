#random模块用来生成一个随机数

import random


# randint(a,b)    用来生成[a,b]的随机整数
print(random.randint(2, 9))     #生成[2,9]的随机整数，包含2同时也包含9

#random（）用来[0,1)的随机浮点数
print(random.random())


#randrange(a,b)  用来生成[a,b)的随机整数
print(random.randrange(2, 9))


#choice用来在可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan', 'lisi', 'jack', 'jerry', 'henry', 'tony']))


#sample用来在可迭代对象里随机抽取n个数据
print(random.sample(['zhangsan', 'lisi', 'jack', 'jerry', 'henry', 'tony'], 2))
