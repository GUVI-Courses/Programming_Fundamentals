# operator assignment
'''
a=10
# a=a+20
a+=20
print(a)

a=100  #again a value is assigned to a=100
# a=a-20
a-=20
print(a)

c=100
c/=20
# c=c/20
print(c)

d=20
d=d%10
print(d)

d=20
d=d%3
print(d)

d=3
d=d**3
# 3*3*3
print(d)
'''
# comparison operators
'''
a=10
b=20
c=20
d=30
print(a<=b)
print(b<=b)
print(a>b)
print(a>d)
print(d>a)
print(a==10)
print(b==c)
print(d==c)
print(a!=b) #not equals ! =
'''
# logical operators
'''
# And Operation
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(False and False and True and True)
print(True and True and True and True )
print(True and True and False and True )
print("\n")
print(10>5 and 20<30 and 10==10)
# print(True and True and True)
print(10>5 and 20>30 and 10==10)
# print(True and False and True)
'''
# or Operation
'''
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(False or False or True or True)
print(True or True or True or True )
print(True or True or False or True )
print("\n")
print(10>5 or 20<30 or 10==10)
# print(True or True or True)
print(10>5 or 20>30 or 10==10)
# print(True or False or True)
print("\n")
print(not True)
print(not False)

'''

# identity 
a=10
b=5
print(a is b)
print(a is not b)

# membership 
a=10
b=[1,2,3,4,5]
print(a in b)
print(a not in  b)

# bitwise
print(1 & 1)
print(1 & 0)
print(1 & 0)
print(0 & 0)
print("\n")
print(1 | 1)
print(1 | 0)
print(1 | 0)
print(0 | 0)