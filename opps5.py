# method overloading

# class A:    
#     def add(self,a,b):
#         res=a+b
#         print("sum of a + b is ",res)

   
#     def add(self,a,b,c):
#         res=a+b+c
#         print("sum of a + b + c is ",res)

    
#     def add(self,a,b,c,d):
#         res=a+b+c+d
#         print("sum of a + b + c + d is ",res)


# obj1=A()
# obj1.add(1,2)

# pip install multipledispatch

from multipledispatch import dispatch


@dispatch(int, int)
def add(a,b):
    res=a+b
    print("sum of a + b is ",res)


@dispatch(int, int,int)   
def add(a,b,c):
    res=a+b+c
    print("sum of a + b + c is ",res)


@dispatch(int, int,int,int)   
def add(a,b,c,d):
    res=a+b+c+d
    print("sum of a + b + c + d is ",res)


add(10,20)
add(10,20,40)
add(10,20,40,50)
