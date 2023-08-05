employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_dict = {employee: defaults.copy() for employee in employees}
print(employee_dict)
