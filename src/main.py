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
    print("\nPrime number p =", p)
    print("\nPrime number q =", q)
    print("\nCalculated n = p * q =", n)
    print("\nCalculated λ(n) = lcm(p-1, q-1) =", λ)
    print("\nChoosen an integer e =", e)
    print("\nCalculated d =", d)
    print("\nRSA public key pair (e, n):", e, n)
    print("\nRSA private key pair (d, n):", d, n)


    print("\nType in message to encrypt: ")
    message_to_encrypt = input()   # initial message to encrypt

    print("\nYou typed in message to encrypt:", message_to_encrypt)

    # Converting each character into ASCII code
    message_ASCII = [ord(ch) for ch in message_to_encrypt]

    # Encrypting message (m ^ e) mod n = message_ASCII
    message_encrypted = [pow(ch, e, n) for ch in message_ASCII]

    print("\nYour message in encrypted form (every character is encrypted and presented in digital form):", message_encrypted)

    print("\nEncryption operation is finished.")

    # Decrypting encrypted message (m ^ d) mod n = message_decrypted_intoASCII
    message_decrypted_intoASCII = [pow(ch, d, n) for ch in message_encrypted]

    # Converting each character from ASCII code
    message_decrypted = "".join(chr(ch) for ch in message_decrypted_intoASCII)

    print("\nYour message decrypted from encrypted form:", message_decrypted)

    print("\nDecryption operation is finished.")


if __name__ == "__main__":
    main()

