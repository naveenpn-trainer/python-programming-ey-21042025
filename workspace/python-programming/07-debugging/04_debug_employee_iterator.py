import data_generator
from custom_objects import Employee
def main():
    employees = data_generator.get_employees()
    for employee in employees:
        print(f"Employee name: {employee.name}, Bonus= {employee.get_bonus()}")

if __name__ == '__main__':
    main()