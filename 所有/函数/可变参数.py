#*args 表示可变参数
#**kwargs 表示可变的关键字参数



def add(a,b,*args, **kwargs):
    #print('a={}, b={}' .format(a,b))
    #print('args={}'.format(args))   #多出来的可变参数会以元组的形式保存到args里

    print('kwargs = {}'.format(kwargs))   #多出来的关键字参数会以字典的形式保存
    c = a + b
    for arg in args:
        c = c + arg
    return c

add(1,3,5,7,mul=2,x=0,y=4)
(add(9, 5, 4, 2, 0))
print(add(9, 5, 4, 3, 1))
print(add(8, 9, 7, 5, 7, 2, 5, 1))