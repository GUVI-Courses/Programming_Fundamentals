'''
target=50
mid=(low+high/2)

if mid==target:
    return mid #search is found

else if mid < target:
    low =mid+1

else:
    high=mid-1

'''

def binarySearch(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        mid_value=arr[mid]
        if mid_value==target:
            return mid
        elif mid_value<target:
            low=mid+1
        else:
            high=mid-1

    return -1



numbers=[1,2,3,4,5,6,7,8,9]
target=7
index=binarySearch(numbers,target)

if index != -1:
    print("The Element is found ", numbers[index])

else:
    print("The element is not found" )