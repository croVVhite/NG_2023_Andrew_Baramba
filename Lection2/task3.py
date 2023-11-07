def isPrime(number):
    divider = 2
    while divider * divider <= number and number % divider != 0:
        divider += 1
    return divider * divider > number

def main():
    numbersArray = [x for x in range(1, int(input("Enter the number up to which you want to see prime numbers: ")) + 1)]

    primeNumbersTable = dict.fromkeys(numbersArray)

    for num in primeNumbersTable.keys():
        if isPrime(num): primeNumbersTable[num] = "is prime" 
        else: primeNumbersTable[num] = "is not prime"

    for key, value in primeNumbersTable.items():
      print("{0}: {1}".format(key,value))

main()