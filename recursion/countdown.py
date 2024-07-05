## 03. Count Down: Write a recursive function that counts down from n to 1.
def countdown(n):
    if n > 0:
        if n == 1:
            print(1)
            return 1
        print (n)
        countdown(n-1)
    else:
        return

print(countdown(10))