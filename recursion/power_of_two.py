#5. Power of Two: Write a recursive function that takes a number n and returns 2 raised to the power of n.

def power_of_two(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_two(n-1)

print(power_of_two(4))