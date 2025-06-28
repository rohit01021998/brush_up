'''
2. Employee Hierarchy

Create an Employee base class. Inherit and create subclasses like Manager, Developer, Intern.

Override a method get_salary() in each subclass.
Add a class method to count total employees.
'''
import random

managers_record = {}
engineers_record = {}
total_head_count = 0
employee_ids = []

class Employee:
    def __init__(self, employee_id, employee_name, employee_age):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_age = employee_age

    def basic_details(self):
        print(f'\nName is: {self.employee_name}')
        print(f'Employee ID is: {self.employee_id}')
        print(f'Employee Age is: {self.employee_age}')

class Engineer(Employee):
    def __init__(self, employee_id, employee_name, employee_age):
        super().__init__(employee_id, employee_name, employee_age)
        self.designation = 'Engineer'
    
    def salary(self, salary=50000):
        print(f'\n{self.employee_name} Earns: {salary}')

class Manager(Employee):
    def __init__(self, employee_id, employee_name, employee_age):
        super().__init__(employee_id, employee_name, employee_age)
        self.designation = 'Manager'
    
    def salary(self, salary=70000):
        print(f'\n{self.employee_name} Earns: {salary}')

def main():
    global total_head_count

    print("\nPlease enter your choice: ")
    print("1. To add an employee")
    print("2. To remove an employee")
    print("3. To check salary")
    print("4. To check details")

    input_num = int(input("Enter: "))
    if input_num == 1:
        print('\nRegister new employee\n')
        name = input('Enter employee name: ')
        id = int(random.randint(1000000, 9999999))
        while id in employee_ids: id = int(random.randint(1000000, 9999999))
        employee_ids.append(id)
        print(f'New employee id is {id}')
        age = int(input('Enter employee age: '))
        designation = input('Enter his designation (Manager/Engineer): ')
        new_employee = Engineer(id, name, age) if designation.casefold() == 'engineer' else Manager(id, name, age)
        if designation.casefold() == 'engineer':
            engineers_record[new_employee.employee_id] = new_employee
        elif designation.casefold() == 'manager':
            managers_record[new_employee.employee_id] = new_employee
        total_head_count+=1

    elif input_num == 2:
        print(f'For reference, Here is the employee ID list: {employee_ids}')
        remove_id = int(input('Enter employee ID: '))
        if remove_id in engineers_record:
            print("\nBelow Employee is being removed")
            print(engineers_record[remove_id].employee_name)
            print(engineers_record[remove_id].designation)
            del engineers_record[remove_id]
            total_head_count-=1
            employee_ids.remove(remove_id)
        elif remove_id in managers_record:
            print("\nBelow Employee is being removed")
            print(managers_record[remove_id].employee_name)
            print(managers_record[remove_id].designation)
            del managers_record[remove_id]
            total_head_count-=1
            employee_ids.remove(remove_id)
        else:
            print('Error: Employee not found')

    elif input_num == 3:
        print(f'For reference, Here is the employee ID list: {employee_ids}')
        salary_id = int(input('Enter employee ID: '))
        if salary_id in engineers_record:
            engineers_record[salary_id].salary()
        elif salary_id in managers_record:
            managers_record[salary_id].salary()
    
    elif input_num == 4:
        print('\n Following is the list of all engineers:')
        for emp_id in employee_ids:
            if emp_id in engineers_record:
                print(f'Name: {engineers_record[emp_id].employee_name}, Emp ID: {engineers_record[emp_id].employee_id}')

        for emp_id in employee_ids:
            if emp_id in managers_record:
                print('\n Following is the list of all managers:')
                print(f'Name: {managers_record[emp_id].employee_name}, Emp ID: {managers_record[emp_id].employee_id}')

if __name__ == "__main__":
    while True: main()