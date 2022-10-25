#生成器，生成一个序列。
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n
#筛选函数
def _not_divisible(n):
    return lambda x:x%n>0
#生成器，返回下一个素数
def primes():
    yield 2
    it =_odd_iter()   #初始序列
    while True:
        n = next(it)   #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)  #构造新序列

#因primes（）也是一个无限序列，是所以调用时需要设置一个退出循环的条件：
#打印1000以内的素数
for n in primes():
    if n <1000:
        print(n)

    else:
        break

