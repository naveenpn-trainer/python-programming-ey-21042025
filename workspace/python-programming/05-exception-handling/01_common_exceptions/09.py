import os

path = "./test_dir/"
print(os.path.isfile(path))

with open(path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)