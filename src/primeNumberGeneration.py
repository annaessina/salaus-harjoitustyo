import random
from checkIfPrimeNumberMillerRabin import checkIfPrimeNumberMillerRabin

# Generating prime number
def primeNumberGeneration(num1, num2):
    primeNumber = random.randint(num1, num2)  
    while not checkIfPrimeNumberMillerRabin(primeNumber):
        primeNumber = random.randint(num1, num2)
    return primeNumber
