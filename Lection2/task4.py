userText = [x for x in input("Input some text: ").lower()]

for letter in userText:
    if letter in ["a", "e", "i", "o", "u", "y", " "]: print(letter, end="")
