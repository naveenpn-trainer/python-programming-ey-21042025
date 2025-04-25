D = {'apples':'red','grapes':'green','oranges':'orange'}

print("Iterating through the key - I")
for k in D:
    print(k)

print("Iterating through the key -II")
for k in D.keys():
    print(k)

print("Iterating only the values")
for v in D.values():
    print(v)


print("Iterating both key and values")
for k,v in D.items():
    print(k,v)