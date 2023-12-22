# Calculating d that is the modular multiplicative inverse of e modulo λ(n).
# a and b are coprimes, i.e., gcd(a, b) = 1.

def calculateD(a, b):
    temp, y, x = b, 0, 1
 
    if (b == 1):
        return 0
 
    while (a > 1):  
        q=a//b
        t = b        
        b = a % b
        a=t
        t = y        
        y=x-q*y
        x = t  
    if (x < 0):
        x = x + temp
 
    return x
