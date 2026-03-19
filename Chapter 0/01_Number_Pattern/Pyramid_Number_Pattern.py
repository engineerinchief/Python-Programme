r = int(input("Enter the no. of rows: "))
for i in range(1, r + 1):
    print(" " * (r - i) + "".join(map(str, range(1, i * 2))))


'''
    1
   123
  12345
 1234567
123456789
'''