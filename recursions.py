# factorial 
'''____________
1! = 1
0! = 1

formula= factorial(5)
n=n*(n-1)!
_____________
5!

n*(n-1)!
5*(5-1)!
5*(4)!

4!
n*(n-1)!
5*4*(4-1)!
5*4*(3)!

3!
n*(n-1)!
5*4*3*(3-1)!
5*4*3*(2)!

2!
n*(n-1)!
5*4*3*2*(2-1)!
5*4*3*2*(1)!

5*4*3*2*1 = 120 '''

def factorial(n):
    if n==1 or n==0:
        return 1
    print(n)
    n=n*factorial(n-1)
    return n

res=factorial(5)
print(res)