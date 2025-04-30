# L = list(range(2,6))
#
# print(L)
# L.append(6)
# L.append(7)
# print(L)
# L.insert(0,1)
# print(L)
L1 = [1,2,3]
L = [4,5,6]
print(L1.append(L)) # [1,2,3,[4,5,6]]
L.extend(L1) # [1,2,3,4,5,6]
print(L)
print(len(L))
