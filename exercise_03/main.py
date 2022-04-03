a = max(False, -3, -4)
b = min(a, 2, 7)
print(b)

a = max(False, -3, -4, 0)
b = min(a, 2, 7)
print(b)

a = max(False, -3, -4, 1)
b = min(a, 2, 7)
print(b)

a = max(True, -3, -4, 1)
b = min(a, 2, 7)
print(b)

a = max(False, -3, -4, True)
b = min(a, 2, 7)
print(b)
