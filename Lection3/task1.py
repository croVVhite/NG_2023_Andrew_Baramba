fileContent = ""

with open('task1.txt', 'r') as f:
    for line in f.readlines():
        fileContent += line

symbolsAmount = dict.fromkeys(set(fileContent), 0)

for letter in fileContent:
    if letter in symbolsAmount.keys():
        symbolsAmount[letter] += 1

print("Amount of every symbol in file: " + str(symbolsAmount))