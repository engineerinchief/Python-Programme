r = int(input("Enter the no. of rows: "))
for i in range(1, r + 1):
    print("  " * (r - i), end="")
    if i == 1 or i == r:
        print("* " * (2 * i - 1))
    else:
        print("* " + "  " * (2 * i - 3) + "* ")