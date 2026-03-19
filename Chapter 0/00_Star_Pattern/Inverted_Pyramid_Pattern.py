r = int(input("Enter the no. of rows: "))
for i in range(r, 0, -1):
    print(" "* (r - i), end="")
    print("*"* (2*i-1), end="")
    print("")