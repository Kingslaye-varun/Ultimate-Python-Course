class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} & the company is {self.company}")
        
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages, here is your language: {self.language}")


class Programmer(Employee,Coder):
    company = "ITC INFOTECH"
    def showLanguage(self):
        print(f"The name is {self.company} & he is good at {self.language} language")
        
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()