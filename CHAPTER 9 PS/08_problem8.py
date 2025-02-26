with open("this.txt") as f:
    content = f.read()

with open("duplicateThis.txt", "w") as f:
    f.write(content)
