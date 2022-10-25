#函数的三要素： 函数名、参数和返回值
#在有一些编程语言里，允许函数重名，在python里不允许函数的重名
#如果重名了，后一个函数覆盖前一个函数


def test(a,b):
    print('hello,a={},b={}'.format(a,b))

# python里函数名也可以理解成为一个变量名
#test = 对应的是一个函数
def test(x):
    print('good,x={}'.format(x))

#test = 5
test(3)


# 定义变量名的时候避免python内置类的函数，不然会覆盖




