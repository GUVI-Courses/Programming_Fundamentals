# pip install xmltodict
import json
import xmltodict

'''

json_string="""
{
"employee":{
"name":"anees",
"salary":"50000",
"job description":{
"role":"Frontend developer",
"department":"FSADM",
"experience":"4"
},
"location":"bangalore"
}
}
"""

print(json_string)
print("reading json with python dictionary")
employeedictionary=json.loads(json_string)
print(employeedictionary)
print(type(employeedictionary))
print("\n")
print("Converting the json to xml")
xml_data=xmltodict.unparse(employeedictionary)
print("xml string is")
print(xml_data)
'''

# store all json data into xml file 

json_string="""
{
"employee":{
"name":"anees",
"salary":"50000",
"job description":{
"role":"Frontend developer",
"department":"FSADM",
"experience":"4"
},
"location":"bangalore"
}
}
"""

print(json_string)
print("reading json with python dictionary")
employeedictionary=json.loads(json_string)
file=open("employeedetails.xml","w")
xmltodict.unparse(employeedictionary,output=file)
file.close()
print("task is done")