r = int(input("Enter the no. of rows: "))
for i in range(r, 0, -1):
    print(*range(1, i + 1))

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''