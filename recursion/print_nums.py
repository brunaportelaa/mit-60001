# 0.1. Print Numbers: Write a recursive function that prints numbers from 1 to n.

def print_nums(n):
    if n == 1:
        print(1)
    else:
        print(n)
        print_nums(n-1)

#print_nums(5)

### alternative solution, prints in from lowest to highest

def print_nums2(n):
    if n > 0:
        print_nums2(n - 1)
        print(n)

print_nums2(4)

##################################################################################