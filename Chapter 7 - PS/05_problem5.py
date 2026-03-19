n = int(input("Enter the number: "))

# Using While Method

i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1

print(sum)

# Using For Method

sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
