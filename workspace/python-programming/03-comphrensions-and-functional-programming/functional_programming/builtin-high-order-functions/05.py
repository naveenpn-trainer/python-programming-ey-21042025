if __name__ == '__main__':
    employees = [
        {"name":"A","age":36,"salary":10},
        {"name":"B","age":28,"salary":20},
        {"name": "C", "age": 29, "salary": 20},
        {"name": "D", "age": 30, "salary": 40},
        {"name": "E", "age": 29, "salary": 40},
    ]
    # top_employee = max(employees, key=lambda s:s["salary"])
    # print(top_employee)
    #
    # top_employee_by_age = max(employees, key=lambda s:s["age"])
    # print(top_employee_by_age)

    top_salary = max(employees, key=lambda s :(s["salary"], -s["age"]))
    print(top_salary)