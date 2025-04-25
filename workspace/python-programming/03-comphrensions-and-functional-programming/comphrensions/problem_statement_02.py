'''

Given a list of number from 1 to 100
create a new list with number which are divisible by 3 and 5
'''

L = list(range(1,101))
E = [e for e in L if e%15==0]
print(E)