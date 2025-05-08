class InvalidAgeException(Exception):
    """
    Exception raised for errors
    """
    pass


def m1():
    age = int(input("Enter your age"))
    if age < 18:
        raise InvalidAgeException
    else:
        print("Eligible to vote")

try:
    m1()
except InvalidAgeException as e:
    print("Error occured")
