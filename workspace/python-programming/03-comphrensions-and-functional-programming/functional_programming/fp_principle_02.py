def greet_hello(name):
    return f"Hello, {name}"

def greet_hi(name):
    return f"Hi, {name}"

def execute(fn, name):
    return fn(name)

print(execute(greet_hi,"Naveen Pn"))
print(execute(greet_hello,"Naveen Pn"))