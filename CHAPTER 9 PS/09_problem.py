with open("this.txt") as f:
    content1 = f.read()

with open("duplicateThis.txt") as f:
    content2 = f.read()
    
if(content1 == content2):
    print("Yes these files are identical")
else:
    print("No, they aren't identical")
