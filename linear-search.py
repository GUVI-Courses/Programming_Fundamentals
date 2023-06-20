def linearSearch(numbers,target):
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i
    return -1


numbers=[5,2,3,8,9,41,58,69]

target= 58
index=linearSearch(numbers,target)

# target= 121
# index=linearSearch(numbers,target)

if index != -1:
    print("The Element is found ", numbers[index])

else:
    print("The element is not found" )