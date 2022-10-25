def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

print(f1(1,2))

print(f1(1,2,c=3))

print(f1(1,2,3,'a','b'))

print(f1(1,2,3,'a','b',x=99))

print(f2(1,2,d=99,ext=None))

args=(1,2,3,4)

kw = {'d':99,'x':'#'}

f1(*args,**kw)


args=(1,2,3)

kw={'d':88, 'x':'#'}

f2(*args,**kw)

