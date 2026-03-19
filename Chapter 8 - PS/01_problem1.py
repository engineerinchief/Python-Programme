a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
def greatest(a, b, c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    elif (c>a) and (c>b):
        return c
    
print("The No. entered are:", "a->", a, "b->", b, "c->", c)
print("The Greatest No. is:", greatest(a, b, c))

print("Shubh Sneh")




