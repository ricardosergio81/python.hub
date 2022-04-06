#What will be the Output?

```
myList = ["python","hub"]
for i in myList:
    myList.append(i.upper())
print(myList)
```

Options:
- [ ] ["python","hub"]

- [ ] ["PYTHON","HUB"]

- [X] Infinite loop

- [ ] None of above

##Alternative solutions
```
myList = ["python", "hub"]
newList = []
for i in myList:
    newList.append(i.upper())
print(newList)
```

```
myList = ["python", "hub"]
for item, val in enumerate(myList):
    myList[item] = myList[item].upper()
print(myList)
```

```
myList = ["python", "hub"]
myList = [x.upper() for x in myList]
print(myList)
```

```
myList = ["python", "hub"]
myList = list(map(str.upper, myList))
print(myList)
```

```
myList = ["python", "hub"]
myList = list(map(lambda x: x.upper(), myList))
print(myList)
```