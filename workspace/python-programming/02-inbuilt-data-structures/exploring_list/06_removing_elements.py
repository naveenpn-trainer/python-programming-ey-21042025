L = [1,1,2,1,5,5]
print(L)
L.remove(2)
print(L)
print(L.pop()) # By default removes last element
print(L)
print(L.pop(0)) # Removes based on the index specified
print(L)

S = set(L)
print(type(S))