 # Calculating first 500 prime numbers
# using Sieve of Eratosthenes algorithm. Number 3571 is 500th prime number.
def calculate500PrimeNumbers():
    primeNumber = [True for i in range(3572+2)]
    i = 2
    while (i * i <= 3572):
        if (primeNumber[i] == True):
            for j in range(i * i, 3572+1, i):
                primeNumber[j] = False
        i += 1
    list500= [] #list contaning first 500 prime numbers
    for i in range(2, 3572):
        if primeNumber[i]:
            list500.append(i) 