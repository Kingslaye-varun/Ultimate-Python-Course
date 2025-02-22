import os

#Specify Directory you want to list
directory_path = '/'

#List all files & directories in the specified path
contents = os.listdir(directory_path)

#Print each file & directory name.
print(contents)