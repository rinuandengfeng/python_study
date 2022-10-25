def log(func):
    def wrapper(*args,**kw):
        print('call %s:'%func.__name__)
        return func(*args,**kw)
    return wrapper

# @log
# def now():
#     print('2015-3-25')

def hi():
    print('1')
f = hi()
print(f.__name__)