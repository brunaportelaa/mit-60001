#9. Write a recursive function to solve the Towers of Hanoi problem.


def hanoi(n, source, target, spare):
    if n == 1:
        print(f"Move disk {n} from {source} to {target}")
        return
    else:
        hanoi(n-1, source, spare, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, spare, target, source)


hanoi(3, 'A', 'C', 'B')