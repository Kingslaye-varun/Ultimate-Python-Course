class Calculator:
    def __init__(self,n):
        self.n = n
        
    @staticmethod
    def square():
        print(f"Square is {n * n}")
        
    def cube(self):
        print(f"Cube is {self.n * self.n * self.n}")
    
    @staticmethod
    def squareRoot():
        print(f"Square-root is {pow(n,1/2)}")
    
n = int(input("Enter your Number: "))
a = Calculator(n)
a.square()
a.cube()
a.squareRoot()
