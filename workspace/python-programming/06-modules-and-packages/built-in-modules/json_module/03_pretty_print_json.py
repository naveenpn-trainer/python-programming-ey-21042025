import json
data = {"name":"Naveen","age":39}
pretty = json.dumps(data, indent=2)
print(pretty)