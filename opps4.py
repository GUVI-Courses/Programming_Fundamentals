# method overriding

class A:
    def add(self):
        a=12
        b=20
        c=a+b
        print("addition of two number",c)

    def sub(self):
        a=12
        b=20
        c=b-a
        print("substraction of two number",c)

class B(A):
    # def add(self):
    #     a=40
    #     b=20
    #     c=a+b
    #     print("addition of two number",c)

    def sub(self):
        a=40
        b=20
        c=b-a
        print("substraction of two number",c)


obj1=B()
obj1.add()
obj1.sub()


obj1=A()
obj1.add()
obj1.sub()
