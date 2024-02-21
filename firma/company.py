class Person:
    count_persons = 0

    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        Person.count_persons += 1


class Employee(Person):
    count_employees = 0

    def __init__(self, firstname, lastname, gender):
        super().__init__(firstname, lastname, gender)
        self.department = None
        Employee.count_employees += 1

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.department.name})"


class Head_of_Department(Employee):
    count_heads_of_departments = 0

    def __init__(self, firstname, lastname, gender):
        super().__init__(firstname, lastname, gender)
        Head_of_Department.count_heads_of_departments += 1


class Department:
    count_departments = 0

    def __init__(self, name, head_of_department):
        self.name = name
        self.head_of_department = head_of_department
        self.employees = []
        self.employees.append(head_of_department)
        Department.count_departments += 1

    def add_employee(self, employee):
        employee.department = self
        self.employees.append(employee)

    def get_strength(self):
        return len(self.employees)

    def get_percentage(self):
        male_employees = sum(employee.gender == "m" for employee in self.employees)
        female_employees = sum(employee.gender == "f" for employee in self.employees)
        return male_employees/len(self.employees), female_employees/len(self.employees)


class Company:
    departments = []

    def __init__(self, name):
        self.name = name

    def add_department(self, department):
        self.departments.append(department)

    def get_departments_strength(self):
        departments_count = {}
        for department in self.departments:
            departments_count[department.name] = department.get_strength()
        department_with_most_employees = max(departments_count, key=departments_count.get)
        return department_with_most_employees

    def get_company_percentage(self):
        males = 0
        females = 0
        for department in self.departments:
            males += department.get_percentage()[0]
            females += department.get_percentage()[1]
        return males/len(self.departments), females/len(self.departments)

