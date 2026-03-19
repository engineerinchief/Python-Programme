r = int(input("Enter the no. of rows: "))
for i in range(r):
    if i == 0 or i == r - 1:
        print("* " * r)
    else:
        print("* " + "  " * (r - 2) + "* ")