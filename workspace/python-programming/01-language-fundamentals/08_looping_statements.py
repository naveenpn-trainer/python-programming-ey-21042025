# str_01 = "ABCDEFG"
# print(str_01[0])
# print(str_01[3])
#
# for e in str_01:
#     print(e)
#
# for e in range(1,11,2):
#     print(e)

# for row in range(0,6):
#     for col in range(0,3):
#         print(row,col,sep="",end="\t")
#     print()

str_02 = "SADCDYT"
is_a_present = False
for e in str_02:
    print(e)
    if e=="A":
        is_a_present=True
        print("A found")
        break
print(is_a_present)
