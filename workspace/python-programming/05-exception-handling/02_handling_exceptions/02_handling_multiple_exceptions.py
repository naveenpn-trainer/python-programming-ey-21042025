def calculate_quotient(first,second):
    print(f"{first} divided by {second} is {first / second}")

def get_max_value(li):
    print(max(li))

if __name__ == '__main__':
    try:
        first = float(input("Enter first number?"))
        second = float(input("Enter second number?"))
        calculate_quotient(first,second)
    except ValueError:
        print("You must enter only numbers")
    except ZeroDivisionError:
        print("Cannot divide a number by zero")

    get_max_value([1,4,2,5,2])
