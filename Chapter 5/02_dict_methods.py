marks = {
    "Prannay": 100,
    "Sanyam": 56,
    "Surya": 23,
    0: "Prannay"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Surya": 99, "Aadya": 100})
print(marks)

print(marks.get("Sanyam")) 
# print(marks.get("Sanyam2")) - Prints None
# print(marks("Sanyam2")) - Returns an error
print(marks["Aadya"]) 

print(len(marks))