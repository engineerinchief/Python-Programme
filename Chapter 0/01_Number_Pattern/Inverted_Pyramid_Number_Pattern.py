r = int(input("Enter the no. of rows: "))
for i in range(r, 0, -1):
    print(" " * (r - i) + "".join(map(str, range(1, i * 2))))

    '''
123456789
 1234567
  12345
   123
    1

    '''