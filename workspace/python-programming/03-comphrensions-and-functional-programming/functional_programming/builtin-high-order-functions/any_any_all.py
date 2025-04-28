numbers = [15,30,45,60]
print(any(x%30==0 for x in numbers))
print(all(x%15==0 for x in numbers))