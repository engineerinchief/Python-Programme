# username = input("Enter username: ")

# if(len(username)<10):
#     print("Your username contains less than 10 characters")
# else:
#     print("Your username contains more than or equal to 10 characters")

a = input("Enter the Username: ")

if(len(a)<=10):
    print("No Objection!!!")
    print("Go Ahead!!!")
elif(len(a)== 0 or len(a)>10 or len(a)<0):
    print("Invalid Username")
    print("Access Denied!!!")    