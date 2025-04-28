dict_01 = {"a":65,"b":66,"c":67}
for k in dict_01.values():
    print(k)

for k,v in dict_01.items():
    print(k,v)


dict_02 = {value:key for key,value in dict_01.items()}
print(dict_01)
print(dict_02)