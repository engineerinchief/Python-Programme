a = "31.2"
b = float(a) # a but the type should be float
c = int(float(a))
t = type(b) 

print(t)
print(type(c))