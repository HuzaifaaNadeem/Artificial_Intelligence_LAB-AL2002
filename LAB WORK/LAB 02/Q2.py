class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

emp1 = FullTimeEmployee("Ali", "K2001", 80000)
emp2 = PartTimeEmployee("Sara", "K2034", 80, 1000)
print(emp1.name, "Salary:", emp1.calculate_salary())
print(emp2.name, "Salary:", emp2.calculate_salary())
