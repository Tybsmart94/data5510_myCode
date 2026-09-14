class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # def __str__(self):
    #     return f"Their name is {self.name} and they make {self.salary}"

    def increase_salary(self):
        new_salary = self.salary * 1.1
        return new_salary

john = Employee("John", 5000)
updated_salary = john.increase_salary()

print(updated_salary)