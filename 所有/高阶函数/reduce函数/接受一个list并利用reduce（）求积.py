from functools import reduce
def pord(L):
    product = 1
    for n in L:
        product = product * n

    return product


print(pord([3,5,7,9]))
