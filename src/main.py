import random
from calculate_gcd import calculate_gcd
from calculateD import calculateD
from checkIfPrimeNumber import checkIfPrimeNumber
from checkIfPrimeNumberMillerRabin import checkIfPrimeNumberMillerRabin
from primeNumberGeneration import primeNumberGeneration

def main():
    # RSA algorithm to generate public and private keys. Source: Wikipedia. RSA (cryptosystem).
    # 1. Generate prime numbers p and q.
    # 2. Calculate n = p*q
    # 3. Calculate Carmichael's totient function λ(n) = lcm(p − 1, q − 1).
    #    lcm(a,b) is the Least common multiple of two integers a and b.
    # 4. Calculating prime number e using greatest common divisor (gcd)
    # 5. Calculate d such as (d*e) mod λ = 1
    # RSA public key is pair e, n
    # RSA private key is pair d, n

    # 1. Generating prime numbers p and q

    # Search for prime number happens in range 2**(1024-1) and 2**1024 - 1.
    # The range can be changed to any (search time increases/decreases accordingly).
    p = primeNumberGeneration(2**(1024-1), 2**1024-1)
    q = primeNumberGeneration(2**(1024-1), 2**1024-1)

    # 2. Calculating n
    n = p * q

    # 3. Calculating λ(n) = lcm(p-1, q-1)
    λ = (p-1)*(q-1)//calculate_gcd(p-1, q-1)

    # 4. Calculating e
    e = random.randint(3, λ-1)
    while calculate_gcd(e, λ) != 1:  
        e = random.randint(3, λ - 1)


    # 5. Calculating d that is the modular multiplicative inverse of e modulo λ(n).
    d = calculateD(e, λ)


    # User interface
    print("For your information: ")
    print("Prime number p =", p)
    print("Prime number q =", q)
    print("Computed n = p * q =", n)
    print("Computed λ(n) = lcm(p-1, q-1) =", λ)
    print("Choosen an integer e =", e)
    print("Determined d =", d)
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

