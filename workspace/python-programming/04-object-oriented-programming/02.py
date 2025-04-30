class Student:
    def __init__(self, roll_no, name):
        # Creating an Instance Variables
        self.roll_no = roll_no
        self.name = name
        self.marks = None

    def set_marks(self, marks):
        self.marks = marks

    def print_details(self):
        details = f''''
        Roll no= {self.roll_no}
        Name= {self.name}
        Marks = {self.marks}
        '''
        print(details)

if __name__ == '__main__':
    s1 = Student(1001,"Naveen Pn")
    # s1.set_marks([100,100,100,100])
    s1.print_details()

