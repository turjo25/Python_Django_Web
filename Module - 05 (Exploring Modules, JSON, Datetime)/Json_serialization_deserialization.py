import json

#Serialization: Python to Json
data = {
    'name' : "Rahim" ,
    'age' : 30,
    'is_logged_in' : True ,
    'test' : None
}
json_string = json.dumps(data,indent=4)
print(json_string, type(json_string))

#Deserialization: Json to Python
data = '{"name" : "Rahim","age" : 30,"is_logged_in" : true,"test": null}'
python_dict = json.loads(data)
print(python_dict,type(python_dict))