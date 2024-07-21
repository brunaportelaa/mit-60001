#Problem 1: Division by Zero
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

#print(divide())

##################################################################################

#Problem 2: File Reading
#Write a function read_file(file_path) that reads the contents of a file specified by file_path and returns its contents.
# Add exception handling to manage cases where the file does not exist or cannot be read.

def read_file(file_path):
    try:
        f = open(file_path, 'r')
        print(f.read())
    except:
        print('Cannot open and read file')

#read_file('existing_file.txt')
#read_file('non_existing_file.txt')

###########################################################

#Problem 3: Implement a function that satisfies the specification
def findAnEven(l):
    """
    Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number
    """
    try:
        for e in l:
            if e % 2 == 0:
                return e
            else:
                raise ValueError
    except ValueError:
        print('The list provided does not include an even number')

has_even_number = [0, 1, 2, 3, 4, 5]
no_even_number = [1, 3, 5, 7]

print(findAnEven(has_even_number))
print(findAnEven(no_even_number))