#def int2(x, base=2):
#    return int(x, base=2)
#print(int2('1000000'))
#print(int2('1010101'))

#functools.partial的作用就是，把一个函数的某些参数给固定注（也就是设置默认值），返回一个新的函数，
#调用这个新函数会更简单。
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
