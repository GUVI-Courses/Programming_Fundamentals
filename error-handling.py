# numerator=int(input("enter numerator value :\n"))
# denominotor=int(input("enter denominotor value :\n"))
# try:
#     print("division of two number is ",numerator/denominotor)

# except:
#     print("error occured i have handled it")

# numerator=int(input("enter numerator value :\n"))
# denominotor=int(input("enter denominotor value :\n"))
# try:
#     print("division of two number is ",numerator/denominotor)

# except:
#     print("error occured i have handled it")

# finally:
#     print("i will execute 100%")

# numerator=int(input("enter numerator value :\n"))
# denominotor=int(input("enter denominotor value :\n"))
# try:
#     print("division of two number is ",numerator/denominotor)

# except Exception as e:
#     print("error occured ",e)

# finally:
#     print("i will execute 100%")


# try:
#     print(12+"anees")
# except Exception as e:
#     print("error ",e)

# try:
#     price=500
#     if price<1000:
#         raise ValueError("please have 1000 rs and come to trip")
#     else:
#         print("you are eligible for trip")

# except ValueError as e:
#     print(e)

# run time errors 
# a=[1,2,34]
# try:
#     print(a[2])
#     print(a[4])
# except Exception as e:
#     print("error",e)

# rasiing own exceptions

# try:
#     raise NameError("Hi anees")
# except NameError as w:
#     print("an exception",w)

# file error

# try:
#     f=open("guvi.txt","r")
# except Exception as f:
#     print("error",f)
# eof error

try:
    n = int(input("enter the number\n"))
    # print(n * 10)
    
except Exception as e:
    print(e)