import os
# indicate path
path = input("enter path ")
# display files in directory
dir_files = os.listdir(path)
# iterate over all elements in dir_files array 
for file_name in dir_files:
# if directory - display as directory
    if os.path.isdir(file_name):
        print("Dir", file_name)
# if file - display file name 
    else:
        print("Fil", file_name)