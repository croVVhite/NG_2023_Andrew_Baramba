firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

operation = input("\nChoose operation (+, -, *, /, ^, root): ").lower()

print("{} {} {} = ".format(firstNumber, operation, secondNumber), end="")

match operation:
    case "+":
        print(str(firstNumber + secondNumber))
    case "-":
        print(str(firstNumber - secondNumber))
    case "*":
        print(str(firstNumber * secondNumber))
    case "/":
        print(str(firstNumber / secondNumber))
    case "^":
        print(str(firstNumber ** secondNumber))
    case "root":
        print(str(firstNumber ** (1/secondNumber)))
    case _:
        print("ERROR!\nInvalid operation value!")