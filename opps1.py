class Human:
    name="rohan"
    age=24,
    height=5.9
    #data members of the class

    # method
    def humanDetails(self):
        print(f"Human name is {self.name}\nAge is {self.age}\nheight is {self.height}")


person1=Human() #person1 is object
print(type(person1))
print(person1)
print(person1.name)
print(person1.age)
print(person1.height)
print()
person1.humanDetails()

