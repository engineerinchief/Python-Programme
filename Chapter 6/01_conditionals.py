a = int(input("Enter your age: "))
if(a==0 or a>120):
    print("You've entered an invalid age")
elif(a<0):
    print("You've entered a negative invalid age")
elif(a>=18):
    print("You're above the age of consent")
    print("Permission Granted!!!")
else:
    print("You're below the age of consent")
    print("Access Denied!!!")

print("The End")

# a = int(input("Enter your age: "))

# if a < 0 or a > 99:
#     print("Not Valid")
# elif a >= 18:
#     print("You're above the age of consent")
#     print("Permission Granted!!!")
# else:
#     print("You're below the age of consent")
#     print("Access Denied!!!")

# print("The End")