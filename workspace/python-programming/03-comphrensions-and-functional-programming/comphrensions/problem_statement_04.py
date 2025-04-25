names = ["Ram","Laxman","Krishna"]
ages = [30,40,50]
E = [(name,age) for name, age in zip(names,ages)]
print(E)
E = [f"{name},{age}" for name, age in zip(names,ages)]
