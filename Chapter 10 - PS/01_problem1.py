
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("Prannay", 10000000,110051)        
r = Programmer("Rohan", 100000,82223)
print(p.name, p.salary, p.pin)
print(r.name, r.salary, r.pin)        
        
