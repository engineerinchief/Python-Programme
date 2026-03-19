class Demo:
    a = 1

b = Demo()
print(b.a) # Prints the class attribute because instance attribute is not present
print(Demo().a)
b.a = 5 # Instance attribute is set
print(b.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute