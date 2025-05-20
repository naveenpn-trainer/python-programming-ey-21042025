class InvalidAgeException(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age: {age}. Must be 18 or older."
        self.log_error()  # Automatically log error on instantiation
        super().__init__(self.message)

    def log_error(self):
        with open("error_log.txt", "a") as file:
            file.write(f"Error: {self.message}\n")


try:
    age = 16
    if age < 18:
        raise InvalidAgeException(age)
except InvalidAgeException as ex:
    print(f"Exception occurred: {ex}")
