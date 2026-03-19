c = float(input("Enter the temperature in °C: "))
def ctof():
    return ((c*1.8) + 32)
e = ctof()
print(c, "°C is equal to", round(e, 2), "°F")


f = float(input("Enter the temperature in °F: "))
def ftoc():
    return ((f-32) / 1.8)
d = ftoc()
print(f, "°F is equal to", round(d, 2), "°C")
