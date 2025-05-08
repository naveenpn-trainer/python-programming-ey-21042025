class InvalidAgeException(Exception):
    pass

try:
    age = int(input("Enter your age"))
    if age < 18:
        raise InvalidAgeException("Invalid age")
    else:
        print("Eligible to vote")
except InvalidAgeException as e:
    print("Exception occured:", e )


