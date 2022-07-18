# inherits, extend, override
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary= salary

    def work(self):
        print(f"{self.name} is working ...")

    # def debug(self):
    #     print(f"{self.name} is debugging...")        
        
class SoftwareEngineer(Employee):
    def __init__(self, name , age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding ...")    

    def deb(self):
        print(f"{self.name} is debugging...")    

class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing ...")  
    
    def draw(self):
        print(f"{self.name} is drawing...")

se = SoftwareEngineer("Max", 25, 6000, "Junior")
# print(se.name, se.age)
# se.work()
# print(se.level)

d = Designer("Phillip", 27, 7000)
# print(d.name, d.age)
# d.work()

# Polymorphism: 

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
            SoftwareEngineer("Lisa", 30 , 9000, "Senior"),
            Designer("Phillips",27,7000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)                    