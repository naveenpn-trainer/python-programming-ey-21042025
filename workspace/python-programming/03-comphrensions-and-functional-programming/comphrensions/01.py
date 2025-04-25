L = list(range(1,11))
# Without comphrensions
E = []
for e in L:
    e+=1
    E.append(e)
print(E)

# With comphrensions
E = [e+1 for e in L]
print(E)
