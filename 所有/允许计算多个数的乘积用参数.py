def product(x,y=1,*nubers):
    sum=x*y
    for n in nubers:
        sum = sum*n
    return sum

print(product(5,6,3,7))