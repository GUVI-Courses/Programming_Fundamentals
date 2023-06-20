import function1
import function2
# import pandas
'''
def greeting():
    print("Good Morning")
    print("Have a nice day")

greeting()
'''

'''
def greeting(name):
    print("Good Morning",name)
    print("Have a nice day")

greeting("Anees")
greeting("Arfa")
greeting("Shuaib")
greeting("Chandan")
'''
'''
def Circle(radius):
    print("the area of a circle is ",3.14*radius*radius)

def square(side):
    print("Area of the square is ",side*side)

def rectangle(length,breadth):
    print("Area of the rectangle is ",length*breadth)


rectangle(10,20)
square(10)
Circle(5)

'''

# function with return

def Employee():
    name=input("Enter the employee name :\n")
    salary=int(input("Enter the employee Salary :\n"))
    return salary,name


sal,name=Employee()
print("employee1 name is ",name,"employee salary is ",sal)

