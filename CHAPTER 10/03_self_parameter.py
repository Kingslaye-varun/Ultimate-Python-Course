class Employee:
    language = "Python"
    salary = 500000.0
    
    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    
    @staticmethod   #Means greet is a static method & doesn't require an Object i.e. no need of self
    def greet():
        print("Good Morning")

Varun = Employee()
Varun.language = "Java"
Varun.greet()
Varun.getInfo()
