userText = [x for x in input("Input some text: ").lower()]
vowels = ["a", "e", "i", "o", "u", "y", " "]

for letter in userText:
    if letter in vowels: print(letter, end="")
