class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is: {self.name} & the salary is {self.salary}")
        
# class Programmer:
#     company = "ITC INFOTECH"
#     def show(self): 
#         print(f"The name is: {self.name} & the salary is {self.salary}")
        
#     def showLanguage(self):
#         print(f"The name is {self.name} & he is good at {self.language} language")

class Programmer(Employee):
    company = "ITC INFOTECH"
    def showLanguage(self):
        print(f"The name is {self.name} & he is good at {self.language} language")
        
a = Employee()
b = Programmer()

print(a.company, b.company)