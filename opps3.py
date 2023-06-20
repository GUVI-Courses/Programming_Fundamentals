class Parent:
    name="parent"

    def propertys(self):
        print("parent property")

    def business(self):
        print("parent business")

    def car(self):
        print("parent car")

class Child(Parent):
    name="child"

    def mobile(self):
        print("child mobile")

    def laptop(self):
        print("child laptop")


# c1=Child()
# c1.propertys()
# c1.business()
# c1.car()
# c1.mobile()
# c1.laptop()
# print(c1.name)

p1=Parent()
p1.business()
p1.propertys()
p1.car()
