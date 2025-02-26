f = open("file.txt")
print(f.read())
f.close()

#Same can be done using with statement
with open("file.txt") as f:
    print(f.read())
