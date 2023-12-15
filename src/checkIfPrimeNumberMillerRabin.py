#Miller-Rabin primality test on whether randomly found number is a prime number
import random, math

def checkIfPrimeNumberMillerRabin(n):
    s = 0
    k = n-1

    while k%2==0:
        k>>=1
        s+=1
    assert(2**s * k == n-1)
 
    def checkIfComposite(a):
        if pow(a, k, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * k, n) == n-1:
                return False
        return True  
 
    for i in range(40):
        a = random.randrange(2, n)
        if checkIfComposite(a):
            return False
 
    return True
