firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

operation = input("\nChoose operation (+, -, *, /, ^, root): ").lower()

match operation:
    case "+":
        resMessage = "{0} {1} {2} = " + str(firstNumber + secondNumber)
    case "-":
        resMessage = "{0} {1} {2} = " + str(firstNumber - secondNumber)
    case "*":
        resMessage = "{0} {1} {2} = " + str(firstNumber * secondNumber)
    case "/":
        resMessage = "{0} {1} {2} = " + str(firstNumber / secondNumber)
    case "^":
        resMessage = "{0} {1} {2} = " + str(firstNumber ** secondNumber)
    case "root":
        resMessage = "{0} {1} {2} = " + str(firstNumber ** (1/secondNumber))
    case _:
        resMessage = "Invalid operation"

print(resMessage.format(firstNumber, operation, secondNumber))