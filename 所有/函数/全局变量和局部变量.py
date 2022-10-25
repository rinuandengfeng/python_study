a = 100  #这个变量是全局变量，在整个py文件里都可以访问
world = '你好'

def test():
    x = 'hello'  #这个变量是在函数内部定义的变量，它是局部变量，只能在函数内部使用
    print('x = {}'.format(x))


    #如果局部变量的名和全局变量同名，会在函数内部有定义一个新的局部变量
    #而不是修改全局变量
    a = 10  # 在函数内部有定义了一个新的局部变量
    print('函数内部a = {}'.format(a))


    #函数内部如果想要修改全局变量？
    #使用global对变量进行声明，可以通过函数修改全局变量的值
    global world
    world = 'ok'
    print('locals = {}, globals = {}'.format(locals(),globals()))

test()
#print(x)   # x只能在函数内部使用
print('函数外部a = {}'.format(a))   #{}  .format()函数用于占位
print('函数外部world = {}'.format(world))



#内置函数globals()  可以查看全局变量 locals()可以查看局部变量


#在python里，只有函数能够分割作用域

