marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

#CHeck for total percentage

total_percentage = (marks1 + marks2 + marks3)/3.0

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You Passed")
else:
    print("You Failed!")