class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) #Prints a
# print(o.b) #shows error

o = Programmer()
print(o.a, o.b)
# print(o.c) shows error

o = Manager()
print(o.a, o.b, o.c)