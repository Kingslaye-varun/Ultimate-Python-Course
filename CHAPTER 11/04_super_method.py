class Employee:
    
    def __init__(self):
        print("Constructor of Employee class called")
    
    a = 1

class Programmer(Employee):
    
    def __init__(self):
        print("Constructor of Programmer class called")
    
    b = 2

class Manager(Programmer):
    
    def __init__(self):
        super().__init__()
        print("Constructor of Manager class called")
    
    c = 3

# o = Employee()
# print(o.a) #Prints a
# # print(o.b) #shows error

# o = Programmer()
# print(o.a, o.b)
# # print(o.c) shows error

o = Manager()
print(o.a, o.b, o.c)