L = list(range(1,11))
E = []
for e in L:
    if e%2==0:
        e+=1
        E.append(e)
print(E)

print("Comphrensions")
E = [e+1 for e in L if e%2==0]
print(E)
