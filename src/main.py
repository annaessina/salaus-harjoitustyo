
import math, random
from calculate_gcd import calculate_gcd
from calculateD import calculateD
from checkIfPrimeNumber import checkIfPrimeNumber
from checkIfPrimeNumberMillerRabin import checkIfPrimeNumberMillerRabin
from primeNumberGeneration import primeNumberGeneration

def main():
    # Algorithm to generate public and private keys
    # 1. Generate prime numbers p and q.
    # 2. Calculate n = p*q
    # 3. Calculate phi = (p-1)*(q-1)
    # 4. Calculating prime number e using greatest common denominator (gcd)
    # 5. Calculate d such as (d*e) mod phi = 1
    # RSA public key is pair e and n
    # RSA private key is pair d and n

    # 1. Generating prime numbers p and q
    p = primeNumberGeneration(2, 10000)
    q = primeNumberGeneration(2, 10000)

    # 2. Calculating n
    n = p * q

    # 3. Calculating phi(n) = (p-1)*(q-1)
    phi = (p-1)*(q-1)

    # 4. Calculating e
    e = random.randint(3, phi-1)
    while calculate_gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)

    # 5. Calculating d such as (d*e) mod phi = 1
    d = calculateD(e, phi)

    # User interface
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


if __name__ == "__main__":
    main()
