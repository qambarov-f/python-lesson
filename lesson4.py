# lesson4

# task1

# tupleData = (
#     "item1",
#     "item2",
#     "item3"
# )
# arr = []

# for items in tupleData:
#     arr.append(items)

# arr.append("item4")
# print(arr)


# --------------------------------------------------------------------------------


# task2

# countDict = {
#     "id": "1",
#     "name": "Hello World",
#     "age": "2"
# }

# enteredCount = int(input("Enter a number, 1: Keys, 2: Values. Your choice is: "))
# if enteredCount == 1:
#     print('keys: ' + str(list(countDict.keys())))  
# elif enteredCount == 2:
#     print('values: ' + ', '.join(countDict.values()))  
# else:
#     print('You entered wrong num, please try again..')

# ------------------------------------------------------------------------------------

# task3

# setFirst = {
#     "red",
#     "black",
#     "yellow"
# }
# setSecond = {
#     "red",
#     "gray",
#     "yellow",
#     "green"
# }

# sameElements = []

# for i in setFirst:
#     for element in setSecond:
#         if i == element:
#             sameElements.append(i)
# print(sameElements)

# ----------------------------------------------------------------

# task4

# keyDict = {
#     "key-1": 1,
#     "key-2": 2,
#     "key-3": 3,
#     "key-4": 4,
#     "key-5": 5
# }

# print(type(keyDict.get("key-1")))
