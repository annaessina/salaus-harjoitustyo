 # Calculating great common divisor (gcd) using extended Euclidean algorithm.

def calculate_gcd(a, b):
  if b == 0:  
    return(a)
  else:  
    while b > 0:
      r = a - b * (a // b)
      a, b = b, r
    return(a)

