def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)

        return move(n-1,c,b,a)
    if n==2:
        print(b,'-->',a)
        return move(n-1,c,a,b)
    if n==3:
        print(b,'-->','c')
        return move(n-1,a,c,b)
    else:
        print()


print(move(3,'A','B','C'))