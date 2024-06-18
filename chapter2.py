a = int(input("Write and Integer number: "))
b = int(input("Write and Integer number: "))
c = int(input("Write and Integer number: "))
print(a, b, c)

if a > b and a > c:
    print(a, "is the biggest number")
elif b > a and b > c:
    print(b, "is the biggest number")
else:
    print(c, "is the biggest number")

print('a' + 'a')