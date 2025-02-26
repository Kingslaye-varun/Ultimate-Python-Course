
with open("log.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes, python word exists in log.txt. Line no: {lineno}")
        break
    lineno += 1
    
else:
        print("No, python word doesn't exist in log.txt")