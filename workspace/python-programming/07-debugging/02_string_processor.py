class StringBuilder:
    def __init__(self,st):
        self.st = st

    def lower_case(self):
        print("lower_case() Invoked")
        self.st = self.st.lower()
        return self

    def upper_case(self):
        print("upper_case() Invoked")
        self.st = self.st.upper()
        return self

    def capitalize(self):
        print("capitalize_case() Invoked")
        self.st = self.st.capitalize()
        return self

    def __str__(self):
        return f"{self.st}"

def process_string(st):
    sb = StringBuilder(st)
    result = sb.lower_case().upper_case().capitalize()
    print(result)

if __name__ == '__main__':
    process_string("abDfgrb")