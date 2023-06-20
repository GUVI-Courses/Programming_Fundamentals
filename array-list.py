'''
myarraylist=[1,2,3,4,5,10,9,8]
print(myarraylist)
print(len(myarraylist))
print(type(myarraylist))
myarraylist.sort()
print(myarraylist)
myarraylist.append(11)
print(myarraylist)
myarraylist.insert(5,6)
print(myarraylist)
myarraylist.pop()
print(myarraylist)
myarraylist.remove(8)
print(myarraylist)
myarraylist.clear()
print(myarraylist)

'''

# items=["apple","orange","grapes"]
# print(items[2])
# print(items[-2])
# list slicing
mylist=[1,2,3,4,5,6,7,8,9,10]
print(mylist[:])
print(mylist[2:5])
print(mylist[:7])
print(mylist[8:])
print(mylist[::-1])
print(mylist[0:11:2])
print(mylist[0:11:3])