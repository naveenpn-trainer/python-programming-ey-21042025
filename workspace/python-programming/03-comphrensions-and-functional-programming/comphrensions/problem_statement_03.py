'''

Given a list of number 1 to 100
if the number is even +1
else add 2
'''

E = [e+1 if e%2==0 else e+2 for e in list(range(1,101))]