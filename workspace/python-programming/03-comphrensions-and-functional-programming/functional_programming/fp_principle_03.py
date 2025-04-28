# Outer Function
def greeting_generator(prefix):
    # Inner Function
    def greet(name):
        return f"{prefix} {name}"
    return greet

say_hi = greeting_generator("Hi")
say_hello = greeting_generator("Hello")

print(say_hi("Naveen Pn"))
print(say_hello("Naveen Pn"))