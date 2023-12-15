 # Since p and q should be prime numbers,
# we have to check whether newly found number is a prime number
def checkIfPrimeNumber(num):
        if num < 2:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True 