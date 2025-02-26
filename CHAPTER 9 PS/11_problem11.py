with open("old.txt") as f:
    content = f.read()

with open("renamed_by_Python.txt", "w") as f:
    f.write(content)
