e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 
f = {"Prannay", "Raju", 4, 5, 3, 5, "Raju"}

print(s, type(s))
print(f, type(f))
s.add("637")
print(f, type(f))
f.remove("Raju")
print(f, type(f))
print(len(s))
print(len(f))