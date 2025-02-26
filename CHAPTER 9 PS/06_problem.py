with open("log.txt") as f:
    content = f.read()
if("python" in content):
    print("Yes, python word exists in log.txt")
else:
    print("No, python word doesn't exist in log.txt")