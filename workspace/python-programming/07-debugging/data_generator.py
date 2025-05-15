from custom_objects import User, Employee
def get_users():
    users = []
    u1 = User("Naveen","naveenpn@gmail.com","IND")
    u2 = User("Praveen", "praveen@gmail.com", "IND")
    u3 = User("Nikshay", "nikshay@gmail.com", "IND")
    u4 = User("Shruthi", "", "IND")
    u5 = User("A", "", "IND")
    u6 = User("B", "", "US")
    u7 = User("C", "", "IND")
    users.append(u1)
    users.append(u2)
    users.append(u3)
    users.append(u4)
    users.append(u5)
    users.append(u6)
    users.append(u7)
    # users.append("Dummy Data")
    return users

def get_employees():
    employess = []
    e1 = Employee("A",10,10000)
    e2 = Employee("B", 10, 10000)
    e3 = Employee("C", 0, 10000)
    e4 = Employee("D", 10, 10000)
    employess.append(e1)
    employess.append(e2)
    employess.append(e3)
    employess.append(e4)
    return employess