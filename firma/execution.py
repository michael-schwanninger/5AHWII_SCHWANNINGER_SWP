import company

if __name__ == "__main__":
    c = company.Company("GeileFirma")

    e1 = company.Employee("Mathias", "Thaler", "m")
    e2 = company.Employee("Hanna", "Schwanninger", "f")
    e3 = company.Employee("Simon", "Trailovic", "m")
    h1 = company.Head_of_Department("Michael", "Schwanninger", "m")
    h2 = company.Head_of_Department("Hans", "Kans", "m")

    d1 = company.Department("IT", h1)
    d2 = company.Department("HR", h2)
    c.add_department(d1)
    c.add_department(d2)

    d1.add_employee(e1)
    d1.add_employee(e2)
    d2.add_employee(e3)

    print("Number of Departments: " + str(company.Department.count_departments))
    print("Number of Employees: " + str(company.Employee.count_employees))
    print("Strongest Department: " + str(c.get_departments_strength()))
    print(e3)
    print(c.get_company_percentage())

