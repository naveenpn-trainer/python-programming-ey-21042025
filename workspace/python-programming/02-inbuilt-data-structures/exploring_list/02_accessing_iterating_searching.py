L = list(range(1,11))
print(L)
print(L[3])
# Accessing a list with an index
print(f"Size: {len(L)}")

print("Iterating a list")
for item in L:
    print(item)

print("Searching element")
print(4 in L)
# Custom Logic to search
# number = 3
# number_found = False
# for e in L:
#     if e == number:
#         number_found=True
#         break