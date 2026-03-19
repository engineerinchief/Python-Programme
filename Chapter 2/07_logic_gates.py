d = input("Enter the first boolean value (True/False): ")
f = input("Enter the second boolean value (True/False): ")

# Convert the input to boolean
d = d.lower() == "true"
f = f.lower() == "true"

print("You entered:")
print("d =", d)
print("f =", f)

# Logical AND
print("Logical AND:", d and f)

# Logical OR
print("Logical OR:", d or f)

# Logical NOT
print("Logical NOT d:", not d)
print("Logical NOT f:", not f)

# Logical XOR
print("Logical XOR:", d != f)
