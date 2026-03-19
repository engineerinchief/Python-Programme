l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print("Hello", name)


l = ["Harry", "soham", "sachin", "Rahul"]
for name in l:
    if name.lower().startswith("s"):
        print("Hello", name)