safety = 0
myList = ["python", "hub"]
for i in myList:
    myList.append(i.upper())
    safety += 1
    if safety == 100:
        break
print(myList)

myList = ["python", "hub"]
newList = []
for i in myList:
    newList.append(i.upper())
print(newList)

myList = ["python", "hub"]
for item, val in enumerate(myList):
    myList[item] = myList[item].upper()
print(myList)

myList = ["python", "hub"]
myList = [x.upper() for x in myList]
print(myList)

myList = ["python", "hub"]
myList = list(map(str.upper, myList))
print(myList)

myList = ["python", "hub"]
myList = list(map(lambda x: x.upper(), myList))
print(myList)
