
# Javascript object Notation  news.api
# json is a dict having lists/dictionary nested in it. its an industrial standard for comm between client and server

import json
employee={
    "eid":101,
    "name":"john",
    "salary":3000,
    "projects":["CMS","GMS"],#one key is a list
    "manager":{"mid":201,"name":"Fionaa"}
}
print(employee)
print(type(employee))

# convert dict into JSON
jsonData=json.dumps(employee)
# jsonData = str(employee) # ERR While De-Serialization
print(jsonData)
print(type(jsonData))

# convert JSON into dictionary
employeeDictionary=json.loads(jsonData)
print(employeeDictionary)
print(type(employeeDictionary))


