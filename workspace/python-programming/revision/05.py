L = [10,11,12,13]
D = {}
for i,v in enumerate(L):
    D[i] = v
print(D)

print({i:v for i,v in enumerate(L)})