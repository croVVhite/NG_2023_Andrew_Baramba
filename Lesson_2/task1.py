userList = [listElement for listElement in input("Enter 10 elements via coma without spaces: ").split(",")]

if len(userList) != 10:
    print("Amount of your elements is " + str(len(userList)) + ", which does not match the request!")
else:
    elementToFind, elementQuantity = input("Enter the element whose quantity you want to find in the list: "), 0
    for element in userList:
        elementQuantity += 1 if element == elementToFind else + 0

    print("There's no such element in list!" if elementQuantity == 0 else "Quantity of " + "\"" + str(elementToFind) + "\"" + ": " + str(elementQuantity))
