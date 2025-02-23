a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("GOOD BOY")

elif(a<0):
    print("You are entering an invalid age")

elif(a == 0):
    print("Your age is zero")

else:
    print("You are below the age of consent")

print("END OF PROGRAM")