a = input("Enter the Boolean Value (True/False): ")
b = input("Enter the Boolean Value (True/False): ")

a = a.lower() == "true"
b = b.lower() == "true"

print("You Entered a: ",a)
print("You Entered: b: ",b)
print("Logical AND: ", a and b)
print("Logical OR: ", a or b)