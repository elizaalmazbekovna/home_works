class Employee:
    emp_count=0
    work_rate=2
    """This code is about employers!"""
    def __init__(self,name, salary):
        self.name=name
        self.salary=salary

    def display_count(self):
        pass

    def  display_employee(self):
        print(f"Мое имя: {self.name}, зарплата:  {self.salary}")


    def change_name(self,new_name):
        print("NAME HAS CHANGED")
        self.name=new_name



    def get_total_salary(self):
        return salary
print(Employee.__doc__)
emp1 = Employee("aaa", 18000)
emp2 = Employee("bbbb", 16000)

print("Emp1: ", emp1.name,emp1.salary, "Emp2: ", emp2.name,emp2.salary)

emp1.display_employee()
emp2.display_employee()
emp1.change_name("CCC")
print("Emp1: ", emp1.name,emp1.salary, "Emp2: ", emp2.name,emp2.salary)
