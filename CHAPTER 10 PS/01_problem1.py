class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = Programmer("Varun", 1200000.0, 421204)
print(p.name, p.salary, p.pin)