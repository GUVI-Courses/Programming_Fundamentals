myelements=[]


def push(num):
    myelements.append(num)
    print("After pushing ", myelements)

def remove():
    myelements.pop()
    print("After popping ",myelements)


for i in range(5):
    n=int(input("enter elements to push in the stack\n"))
    push(n)

for i in range(3):
    n=int(input("press 1 to pop\n"))
    if n==1:
        remove()
    