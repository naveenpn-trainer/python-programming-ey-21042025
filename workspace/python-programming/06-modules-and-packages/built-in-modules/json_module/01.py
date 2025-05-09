import json

data = {"name":"Naveen","age":39}

#  Converts dictionary to JSON String
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# Convert JSON String to Dictionary
parsed_dict = json.loads(json_str)
print(parsed_dict)
print(type(parsed_dict))

