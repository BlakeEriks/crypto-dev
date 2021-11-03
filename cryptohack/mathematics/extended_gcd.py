# Let a and b be positive integers.

# The extended Euclidean algorithm is an efficient way to find integers u,v such that

# a * u + b * v = gcd(a,b)

#  Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.

# Using the two primes p = 26513, q = 32321, find the integers u,v such that

# p * u + q * v = gcd(p,q)

# Enter whichever of u and v is the lower number as the flag.

#  Knowing that p,q are prime, what would you expect gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page.

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

print (egcd(26513,32321))