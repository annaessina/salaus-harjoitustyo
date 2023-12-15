 # Calculating gcd using Euclidean algorithm
def calculate_gcd(a, b):
    while(b):
       a, b = b, a % b
    return abs(a) 