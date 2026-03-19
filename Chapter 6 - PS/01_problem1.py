a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

print("The Number enterd first is:", a)
print("The Number enterd second is:", b)
print("The Number enterd third is:", c)
print("The Number enterd fourth is:", d)

# if(a>b and a>c and a>d):
#     print("The Number enterd first is the greatest:", a)
# elif(b>a and b>c and b>d):
#     print("The Number enterd second is the greatest:", b)
# elif(b>a and b>c and b>d):
#     print("The Number enterd third is the greatest:", c)
# elif(d>a and d>b and d>c):
#     print("The Number enterd fourth is the greatest:", d)
# else:
#     print("The Numbers enterd are equal:", a, b, c, d)



if a == b == c == d:
    print("All numbers are equal:", a, b, c, d)
elif a >= b and a >= c and a >= d:
    if a == b or a == c or a == d:
        print("The greatest number is", a, "which was entered more than once")
    else:
        print("The Number entered first is the greatest:", a)
elif b >= a and b >= c and b >= d:
    if b == a or b == c or b == d:
        print("The greatest number is", b, "which was entered more than once")
    else:
        print("The Number entered second is the greatest:", b)
elif c >= a and c >= b and c >= d:
    if c == a or c == b or c == d:
        print("The greatest number is", c, "which was entered more than once")
    else:
        print("The Number entered third is the greatest:", c)
else:
    if d == a or d == b or d == c:
        print("The greatest number is", d, "which was entered more than once")
    else:
        print("The Number entered fourth is the greatest:", d)

