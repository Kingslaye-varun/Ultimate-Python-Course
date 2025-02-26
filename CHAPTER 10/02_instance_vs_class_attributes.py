class Employee:
    language = "Python"
    salary = 500000.0

Varun = Employee()
Varun.language = "Java"
print(Varun.language, Varun.salary)

#Instance Attributes take over class attributes during assignment & retrieval