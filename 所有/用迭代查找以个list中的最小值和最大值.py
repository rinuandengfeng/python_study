def findMinAndMax(L):
    min = 0
    max = 0
    for x in L:

        if max  <= x :
            max = x
        else:
            min = x
    return ('max:',max,'min:',min)

print(findMinAndMax([2,4,6,1,7]))