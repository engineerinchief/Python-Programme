class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    salary = 20000000

    def getInfo(self):
       print("The name, languages and salary is:", self.name, self.language, self.salary)
       print(f"The name, languages and salary is: {self.name}, {self.language}, {self.salary}")
    def greet(self):
       print("Namaste")

Prannay = Employee()
Prannay.name = "Prannay"
Prannay.language = "Hindi" # This is an instance attribute
Prannay.salary = 10000000000
Prannay.greet()
Prannay.getInfo()