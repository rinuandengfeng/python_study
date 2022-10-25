L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s,str) is True else s for s in L1 ]
print(L2 )