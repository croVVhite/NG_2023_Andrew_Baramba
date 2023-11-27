userArray, digitAmount = [element for element in input("Input any elements in array via coma: ").split(',')], 0
for element in userArray:
    if element.isdigit(): digitAmount += 1
print("There is " + str(digitAmount) + " digits in your array")