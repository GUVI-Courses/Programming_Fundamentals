# constructor with class and objects
class Employee:
    company="GUVI" #data members

    # constructor : it is method which is getting called to set the datamembers of the class whenever the object is created
    def __init__(self,name,role,salary):
        # print("i am running constructur")
        self.name=name
        self.role=role
        self.salary=salary

    def employeeDetails(self):
        print(f"\nCompany is {self.company}\nEmployee name is {self.name}\nEmployee role is {self.role}\nSalary is {self.salary}")


emp1=Employee("anees","developer",50000)
emp2=Employee("arfa","frontend developer",90000)
emp3=Employee("chandan","backend developer",150000)
# obj1=Employee()
# obj2=Employee()
# obj3=Employee()

emp1.employeeDetails()
emp2.employeeDetails()
emp3.employeeDetails()