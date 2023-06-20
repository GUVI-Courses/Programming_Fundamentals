# s=set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(1)
# s.add(2)
# s.add(4)
# print("sets items ",s)

# s={1,2,34,1233,12,12,1,4,6}
# print(type(s))
# print(s)

s1={1,2,3,4}
s2={3,4,5,6,7,8,9}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.pop())
print(s1.pop())
print(s2.remove(8))
print(s2)
print(s1.clear())