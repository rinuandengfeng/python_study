import math
def que(a,b,c):
    if a == 0:
        print('input error')
        return
    else:
        nx = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        ny = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return nx, ny

print(que(-2,2,1))