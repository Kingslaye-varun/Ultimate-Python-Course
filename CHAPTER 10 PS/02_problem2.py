class Calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"Square is {self.n * self.n}")
    def cube(self):
        print(f"Cube is {self.n * self.n * self.n}")
        
    def squareRoot(self):
        print(f"Square-root is {self.n ** 1/2 }")
    
n = int(input("Enter your Number: "))
a = Calculator(n)
a.square()
a.cube()
a.squareRoot()
