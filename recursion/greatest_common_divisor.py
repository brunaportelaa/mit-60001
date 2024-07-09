#7. GCD (Greatest Common Divisor): Write a recursive function to find the GCD of two numbers.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48, 18))

#this follows the eucliden algorithm for finding GCD