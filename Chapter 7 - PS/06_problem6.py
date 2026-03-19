n = int(input("Enter the number: "))

''' For Method '''

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"The Factorial of {n} is {factorial}")
print("The Factorial of", n,"is", factorial )

''' While Method '''

i = 1
factorial = 1
while(i<=n):
    factorial = factorial * i
    i += 1
print(f"The Factorial of {n} is {factorial}")
print("The Factorial of", n,"is", factorial )



