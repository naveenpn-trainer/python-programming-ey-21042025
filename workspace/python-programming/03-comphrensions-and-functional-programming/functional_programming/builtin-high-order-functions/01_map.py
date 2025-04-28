def mul_by_2(e):
    return e*2


L = list(range(1,11))
print(list(map(lambda e:e*2,L)))
print(list(map(mul_by_2,L)))