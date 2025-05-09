import json

def write_json(file_name,data):
    with open(file_name,"w") as file:
        json.dump(data, file)

def read_json(file_name):
    content = None
    with open(file_name) as file:
        content = json.load(file)
    return content

if __name__ == '__main__':
    write_json("users.json",data = {"name":"Naveen","age":39})
    print(read_json("users.json"))