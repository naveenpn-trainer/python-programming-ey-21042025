import json

data = {"z":78,"a":23,"d":45,"g":89}
print(data)
sorted_json = json.dumps(data, sort_keys=True)
print(sorted_json)