def foo():
    r = some_function()
    if r == (-1):
        return (-1)

    return r


def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass


# try...except...finally...

try:
    print('try...')
    r = 10 / 0
    print('result:', r)

# 如果没有错误，except语句块不会被执行，但是finally如果有，则一定会被执行

except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
# 可以有多个except来捕获不同类型的错误
except ValueError as e:
    print('VlueError:', e)
except ZeroDivisionError as e:
    print('ZeroDicisionError:', e)
finally:
    print('finally...')
print('END')
