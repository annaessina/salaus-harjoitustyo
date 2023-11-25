import math, random

#Miller-Rabin primality test on whether randomly found number is a prime number
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
 
    for i in range(10):
        a = random.randrange(2, n)
        if checkIfComposite(a):
            return False
 
    return True
 

# Generating prime number
def primeNumberGeneration(num1, num2):
    primeNumber = random.randint(num1, num2)  
    #while not checkIfPrimeNumber(primeNumber):
    while not checkIfPrimeNumberMillerRabin(primeNumber):
        primeNumber = random.randint(num1, num2)
    return primeNumber

# Calculating d
def calculateD(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d

# Generating p and q
p = primeNumberGeneration(2, 10000)
q = primeNumberGeneration(2, 10000)

# Calculating n
n = p * q

#Calculating phi(n) = (p-1)*(q-1)
phi = (p-1)*(q-1)

# Choosing e
e = random.randint(3, phi-1)
while math.gcd(e, phi) != 1:
    e = random.randint(3, phi - 1)


d = calculateD(e, phi)

print("For your information: ")
print("Prime number p =", p)
print("Prime number q =", q)
print("n = p * q =", n)
print("Phi(n) = (p-1) * (q-1) =", phi)
print("e =", e)
print("d =", d)
print("RSA public key pair (e, n):", e, n)
print("RSA private key pair (d, n):", d, n)


print("\nType in message to encrypt: ")
message = input()

print("\nYou typed in message to encrypt:", message)

# Converting each character into ASCII code
message_encoded = [ord(ch) for ch in message]

# Encrypting message (m ^ e) mod n = c
c = [pow(ch, e, n) for ch in message_encoded]

print("\nYour message in encrypted form (on character by character basis):", c)

#Decrypting encrypted message (m ^ d) mod n = m_encoded
m_encoded = [pow(ch, d, n) for ch in c]
message2 = "".join(chr(ch) for ch in m_encoded)

print("\nYour message decrypted from encrypted form above:", message2)









