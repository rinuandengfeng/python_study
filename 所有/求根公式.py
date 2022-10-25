import math
def quadratioc(a,b,c):
    if a==0:
            print("input error")
            return print('a=',a)
    else:
        x = (-b + math.sqrt(b**2-4*a*c))/(2*a)

        y = (-b - math.sqrt(b**2-4*a*c))/(2*a)
        return x,y

print(quadratioc(-2,3,1))

