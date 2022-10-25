def test(a):
    print('修改前a的内存地址0x%X' %id(a))

    a = 100
    print('修改后a的内存地址0x%X' % id(a))



def demo(nums):
    print('修改前nums的内存地址0x%X' % id(nums))
    nums[0] = 10
    print('修改后a的内存地址0x%X' % id(nums))


x = 1
print('修改前x的内存地址0x%X' %id(x))
test(x)
print('修改后的内存地址0x%X' %id(x))
print(x)  #   1


y = [3,5,6,8,2]
print('修改前y的内存地址0x%X' %id(y))
demo(y)
print('修改后y的内存地址0x%X' %id(y))
print(y)   #[10, 5, 6, 8, 2]