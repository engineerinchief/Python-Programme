r = int(input("Enter the number: "))
for i in range(r):
    print(*([i + 1] * (r - i)))


'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''