from functools import reduce

numbers = [1,2,3,4]

print("Imperative style")
result = 0
for number in numbers:
    result += number ** 2
print(result)

print("Declarative style")
result = reduce(lambda  acc, x:acc+x**2,numbers,0)
print(result)