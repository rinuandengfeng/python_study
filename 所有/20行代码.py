def fac(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x
y = fac(5)
print(y)
def fac_sum(m):
    x = 0
    for i in range(1, m+1):
        x = x + fac(i)
    return x
z = fac_sum(3)
print(z)
def add(a,b,*args, **kwargs):
    print('kwargs = {}'.format(kwargs))
    c = a + b
    for arg in args:
        c = c + arg
    return c
s = add(1,2,3,4,5,6,x = 1,f = 3)
print(s)






