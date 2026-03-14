import os

file_path = "main.txt"


if os.path.exists(file_path):
    print(f"this file'{file_path}'is exists")
    with open(file_path,"r") as file:
        content = file.read()
        print(content)
else:
    print(f"this file'{file_path}'dosen't exists")