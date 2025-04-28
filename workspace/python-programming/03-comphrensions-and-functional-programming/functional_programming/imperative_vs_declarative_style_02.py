L = list(range(1,11))
print(L)
print("Imperative Style")
E = []
for e in L:
    E.append(e*3)
print(E)

print('Declarative Style')
E = list(map(lambda e:e*3, L))
print(E)