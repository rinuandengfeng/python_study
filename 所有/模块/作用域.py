# 正常的函数和变量名是公开的，可以被直接引用，ps：abc，x123，PI等；
# 类似_xxx_这样的变量是特殊变量，可以直接被引用，但是有特殊用途，比如上面的__author__,__name__就是特殊变量，我们自己的变量一边不熬用这种变量名
# 类似_xxx和__xxx这样额函数或变量就是非公开的，不应该被直接引用，例：_abc,__abc
# 非公开的不是不能使用，编程习惯不建议使用

def _private_1(name):
    return 'hello, %s' % name


def _private_2(name):
    return 'Hi,%s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



#外部不需要引用的函数全部定义成私人的（private），只有外部需要引用的函数才定义为公开的