a = True
b = False
print(a or a and b and a)

a = True
b = False
print(a or (a and b and a))

a = True
b = False
print((a or a) and b and a)

