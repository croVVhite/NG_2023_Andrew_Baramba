conversion = input("Do you want to convert from Celsius to Fahrenheit (enter \"F\" or \"f\") or from Fahrenheit to Celsius (enter \"C\" or \"c\"): ")

if conversion == "F" or conversion == "f":
    celsius = int(input("Input temperature in Celsius degrees: "))
    print(str(celsius) + " degrees Celsius is " + str(celsius * 1.8 + 32) + " degrees Fahrenheit")
elif conversion == "C" or conversion == "c":
    fahrenheit = int(input("Input temperature in Fahrenheit degrees: "))
    print(str(fahrenheit) + " degrees Fahrenheit is " + str(((fahrenheit - 32)/1.8)) + " degrees Celsius")
else:
    print("Invalid value! Program has been stopped!")