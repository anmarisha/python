import os
path = input("enter path ")
dir_files = os.listdir(path)
for file_name in dir_files:
    if os.path.isdir(file_name):
        print(file_name)
    else:
        print("Fil", file_name)