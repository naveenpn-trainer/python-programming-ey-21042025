L = [
    [1,2,3],
    [4,5,6]
]
print(L)
print(L[0][1])

print("Iterating Nested List")
for row in L:
    for col in row:
        print(f"{col}", sep="", end="\t")
    print()