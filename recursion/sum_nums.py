## 02. Sum of First N Natural Numbers: Write a recursive function to find the sum of the first n natural numbers.

def sum_nums(n):
    if n == 1:
        return 1
    return n + sum_nums(n-1)

print(sum_nums(5))