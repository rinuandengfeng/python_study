"""def is_odd(n):
    return n%2==1

L=list(filter(is_odd,range(1,20)))

print(L)"""

#用匿名函数改上面的函数
f=list(filter(lambda n:n%2==1,range(1,20)))
print(f)
print(list(filter(lambda n:n%2==1,range(1,20))))