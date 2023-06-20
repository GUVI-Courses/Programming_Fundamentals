mydict={
    "name":"Guvi",
    "since":2014,
    "courses":["python","java","javascript"],
    "isActive":True,
    
}

print(mydict)
print(type(mydict))
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(mydict.get("courses"))
mydict.update({"location":"chennai"})
print(mydict)