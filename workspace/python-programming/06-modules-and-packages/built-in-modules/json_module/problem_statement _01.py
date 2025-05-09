import json
import statistics

employees = None
with open("employee.json", "r") as file:
    employees = json.load(file)
    print(type(employees))
    print(employees)

#  Filter only active employees
for e in employees:
    if e["active"]:
        print(f"Name= {e['name']}, Department= {e['department']}")

# Using Comprehension
active_employees = [f"Name={e['name']}- Department={e['department']}" for e in employees if e['active']]
print(active_employees)

#  Calculate average salary of active employees
active_employees = [e['salary']for e in employees if e["active"]]
print(statistics.mean(active_employees))

print(sum(active_employees)/len(active_employees))

# Sort Active Employees by salary (Descending)

active_employees = [e for e in employees if e["active"]]
print(active_employees)
# print(sorted(active_employees, reverse=True))