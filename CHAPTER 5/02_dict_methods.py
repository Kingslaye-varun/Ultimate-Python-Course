marks = {
    "Varun": 100,
    "Atharva": 95,
    "Aayush": 56
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Varun": 99,"Tanaya": 100})
print(marks)

print(marks.get("Varun"))#If key doesnt exists returns None