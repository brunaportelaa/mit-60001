#Problem 1.1: Division by Zero
#Write a function divide(a, b) that takes two arguments, a and b, and returns the result of dividing a by b.
#Add exception handling to catch division by zero errors and print an appropriate message.

def divide():
    """
    Assumes provided parameters are integers
    Returns a divided by b
    """
    while True:
        try:
            a = int(input('Please type an integer number: '))
            b = int(input('Please type another integer number: '))
            result = a/b
            return result
        except ValueError:
            print('Input not supported. Please type a valid integer.')
        except ZeroDivisionError:
            print('Cannot divide by zero, please try again.')

print(divide())