import time


def cal_time(fn):
    # print('cal_time')

    def inner():
        start = time.time()

        fn()
        end = time.time()
        print('代码耗时',end - start)

    return inner()

@cal_time    #第一件事调用cal_time；第二件事把装的函数传递给fn   语法糖
def demo():
    x = 0
    for i in range(1,100):
        x +=i
    print(x)

#第三件事：当再次调用demo函数时，才是的demo函数已经不再是上面的demo

print('装饰后的demo = {}'.format(demo))
print(demo())
