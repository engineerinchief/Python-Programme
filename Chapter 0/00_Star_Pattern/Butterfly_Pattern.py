r = int(input("Enter the number of rows: "))
for i in range(1, r + 1):
    print("* " * i + "  " * (r - i) * 2 + "* " * i)

for i in range(r - 1, 0, -1):
    print("* " * i + "  " * (r - i) * 2 + "* " * i)





# r = int(input("Enter the number of rows: "))
# for i in range(1, r + 1):
#     print("* " * i + "  " * (r - i) + "* " * i)
# for i in range(r - 1, 0, -1):
#     print("* " * i + "  " * (r - i) + "* " * i)
