def normalize(name):
    name1=name.capitalize()
    return name1

L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)