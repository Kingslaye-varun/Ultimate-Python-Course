class Employee:
    a = 1
    b = 2
    def showB(self):
        print(f"The class value of b is: {self.b}")
    
    @classmethod
    def showA(cls):
        print(f"The class attribute of a is: {cls.a}")
        
e = Employee()
e.a = 45
e.b = 65
e.showA()
e.showB()