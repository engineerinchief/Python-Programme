# marks1 = int(input("Enter Marks 1: "))
# marks2 = int(input("Enter Marks 2: "))
# marks3 = int(input("Enter Marks 3: "))

# # Check for total percentage
# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed:", total_percentage)

# else:
#     print("You failed, try again next year:", total_percentage)



a = int(input("Enter the first marks: "))
b = int(input("Enter the second marks: "))
c = int(input("Enter the third marks: "))

percentage = ((100*(a+b+c))/300)

print("The marks enterd first is:", a)
print("The marks enterd second is:", b)
print("The marks enterd third is:", c)

if(percentage>=90 and a >= 83 and b >= 83 and c >= 83):
    print("Waah Mere bete!!!, jitne marks laaya hai utna toh dettol germs bhi nhi maarta")
elif(percentage>=50 and a > 43 and b > 43 and c > 43):
    print("Guiyan Kuch nhi ukhada paper me")
elif(percentage>=40 and a > 33 and b > 33 and c > 33):
    print("Jaa Bhosdike, Pass kiya tujhe!!!")
else:
    print("Yeh lo juta, maaro saale ko!!")
