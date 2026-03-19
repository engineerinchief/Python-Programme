# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")



n = int(input("Enter the Number: "))

for i in range(2,n):
    if (n%i) == 0:
        print("The enterd number isn't prime")
        break
else:
        print("The Number is prime")