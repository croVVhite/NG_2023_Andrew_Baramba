firstNumber, secondNumber = int(input("Enter first number: ")), int(input("Enter second number: "))
operation = input("\nChoose operation (+, -, *, /, square, root): ")

match operation:
    case "+":
        print(str(firstNumber) + " + " + str(secondNumber) + " = " + str(firstNumber + secondNumber))
    case "-":
        print(str(firstNumber) + " - " + str(secondNumber) + " = " + str(firstNumber - secondNumber))
    case "*":
        print(str(firstNumber) + " * " + str(secondNumber) + " = " + str(firstNumber * secondNumber))
    case "/":
        print(str(firstNumber) + " / " + str(secondNumber) + " = " + str(firstNumber / secondNumber))
    case "square":
        print(str(firstNumber) + " ^ " + str(secondNumber) + " = " + str(firstNumber ** secondNumber))
    case "root":
        print(str(secondNumber) + "th root of " + str(firstNumber) + " = " + str(firstNumber ** (1 / secondNumber)))
    case _:
        print("Invalid operation value!")
