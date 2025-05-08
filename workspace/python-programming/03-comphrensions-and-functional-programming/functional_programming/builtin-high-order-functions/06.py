if __name__ == '__main__':
    employees = [
        {"name":"A","age":36,"salary":10},
        {"name":"B","age":28,"salary":20},
        {"name": "C", "age": 29, "salary": 20},
        {"name": "D", "age": 30, "salary": 40},
        {"name": "E", "age": 29, "salary": 40},
    ]

    sorted_employees = sorted(employees, key=lambda e:(-e["salary"], e["age"]))
    for e in sorted_employees:
        print(e)