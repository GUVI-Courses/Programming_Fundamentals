# if statement
# name="Anees"
# salary=10000
# if(salary>5000):
#     print("name is ",name,"salary is ",salary)

# name="Anees"
# salary=10000
# if(salary>15000):
#     print("name is ",name,"salary is ",salary)
#     print("ok i have executed if")

# print("i am outside if statement")
# print("sum of 10 and 20 is ",30)
'''
age=int(input("enter your age:\n"))
if(age>18):
    print("Your age is ",age)
    print("you can vote in elections")

else:
    print("You cannot vote")

print("\n")
print("End if-else")

'''
'''
age=int(input("enter your age:\n"))
if(age>=18 and age<=100):
    print("Your age is ",age)
    print("you can vote in elections")

elif(age==18):
    print("you can vote if you have voter id")

elif(age>100 or age<1):
    print("please give a valid input")

else:
    print("You cannot vote")

print("\n")
print("End if-elseif and else")

'''

'''
int day = 4;
switch (day) {
  case 1:
    System.out.println("Monday");
    break;
  case 2:
    System.out.println("Tuesday");
    break;
  case 3:
    System.out.println("Wednesday");
    break;
  case 4:
    System.out.println("Thursday");
    break;
  case 5:
    System.out.println("Friday");
    break;
  case 6:
    System.out.println("Saturday");
    break;
  case 7:
    System.out.println("Sunday");
    break;

   default:
     System.out.println("tuesday");
    
}
// Outputs "Thursday" (day 4)


'''


# nested if else statement

number=15

if(number<10):
    print("i am in if")

    if(number>5):
        print("i am in nested if of if")
        if(True):
            print("True")
        else:
            print("False")
    else:
        print("i am in nested else of if")

else:
    print("i am in else")

    if(True):
        print("i am else of nested if statement")
    else:
        pass