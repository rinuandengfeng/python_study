#print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
def f(x):
    ax=1
    for i in x:
        ax=ax*i
    return x*x
print(f())