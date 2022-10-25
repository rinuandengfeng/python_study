__all__ = ['m', 'test']  # 只导入__all__里面的变量或方法
m = 'yes'
n = 100


def test():
    print('我是demo模块的test方法')


def foo():
    print('我是demo模块里的foo方法')


def division(a, b):
    return a / b


# __name__：直接运行这个py文件的时候，只是__main__
# 如果这个py文件作为一个模块导入的时候，值是文件名
if __name__ == '__main__':
    print('demo里的name是：', __name__)
    print('测试以下division函数，结果是：', division(4, 2))
