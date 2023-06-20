def euclid(a,b):
    while b!=0:
        a,b=b,a%b 
    return a

num1=14
num2=3
gcd= euclid(num1,num2)
print(f"GCd of {num1} and {num2} is ",gcd)    