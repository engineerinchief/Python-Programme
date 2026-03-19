# marks = []

# f1 = int(input("Enter Marks here: "))
# marks.append(f1)
# f2 = int(input("Enter Marks here: "))
# marks.append(f2)
# f3 = int(input("Enter Marks here: "))
# marks.append(f3)
# f4 = int(input("Enter Marks here: "))
# marks.append(f4)
# f5 = int(input("Enter Marks here: "))
# marks.append(f5)
# f6 = int(input("Enter Marks here: "))
# marks.append(f6)

# marks.sort()

# print(marks)


# marks = []

# mark1 = int(input("Enter the first mark: "))
# mark2 = int(input("Enter the second mark: "))
# mark3 = int(input("Enter the third mark: "))
# mark4 = int(input("Enter the fourth mark: "))
# mark5 = int(input("Enter the fifth mark: "))
# mark6 = int(input("Enter the sixth mark: "))

# marks.append(mark1)
# marks.append(mark2)
# marks.append(mark3)
# marks.append(mark4)
# marks.append(mark5)
# marks.append(mark6)

# print("The first mark is:", mark1)
# print("The second mark is:", mark2)
# print("The third mark is:", mark3)
# print("The fourth mark is:", mark4)
# print("The fifth mark is:", mark5)
# print("The sixth mark is:", mark6)


# print(marks)
# print("Sorted Marks are:", sorted(marks))

# marks.sort()
# print("Sorted Marks are:", marks)


marks = []
marks.append(int(input("Enter the first mark: ")))
marks.append(int(input("Enter the second mark: ")))
marks.append(int(input("Enter the third mark: ")))
marks.append(int(input("Enter the fourth mark: ")))
marks.append(int(input("Enter the fifth mark: ")))
marks.append(int(input("Enter the sixth mark: ")))

print("The first mark is:", marks[0])
print("The second mark is:", marks[1])
print("The third mark is:", marks[2])
print("The fourth mark is:", marks[3])
print("The fifth mark is:", marks[4])
print("The sixth mark is:", marks[5])

print("Original Marks are:", marks)

marks.sort()
print("Sorted Marks are:", marks)


# Sort in ascending order
marks_ascending = sorted(marks)
print("Marks in Ascending Order are:", marks_ascending)

# Sort in descending order
marks_descending = sorted(marks, reverse=True)
print("Marks in Descending Order are:", marks_descending)