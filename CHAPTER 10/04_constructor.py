class Employee:
    
    def __init__(self,name, language, salary):         #Dunder Method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
    
    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    
    @staticmethod   #Means greet is a static method & doesn't require an Object i.e. no need of self
    def greet():
        print("Good Morning")

Varun = Employee("Varun","Python",500000.0)
print(Varun.name,Varun.language,Varun.salary)

Atharva = Employee("Atharva","Javascript",500000.0)
print(Atharva.name, Atharva.language, Atharva.salary)
