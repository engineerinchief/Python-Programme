class Employee:
    language = "Python" # This is a class attribute
    salary = 1000000

Prannay = Employee()
Prannay.name = "Prannay"
Prannay.language = "Hindi" # This is an instance attribute
Prannay.salary = 10000000

print(Prannay.name.title(),Prannay.language,Prannay.salary)