D = {'apple':'red','grapes':'green'}
print(type(D))

D = dict(apples='red',grapes='green')
print(type(D))

key_pair = [('k1',1),('k2',2)]
D = dict(key_pair)
print(D)
print(type(D))

key_pair = [('k1',1),('k2',2)]
D = dict(key_pair,apples='red')
print(D)