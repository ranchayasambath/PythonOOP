class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    # getter
    @property
    def salary(self):
        return self._salary

    # setter
    @salary.setter
    def salary(self, value):
        self._salary = value

    # @salary.deleter
    # def salary(self, value):
    #     self._salary = value    

se = SoftwareEngineer()

se.salary = (6000)

print(se.salary)





