def add_five(n):
    return n+5

x = lambda n : n+5
print(x(4))

result = lambda x,y : x+y
print(result(3,4))


print(list(map(lambda e:e+5, list(range(1,11)))))
