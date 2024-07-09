#6. Palindrome Check: Write a recursive function to check if a string is a palindrome.

def palindrome(s):
    if len(s) == 1 or len(s) == 0:
        return
    else:
        if s[0] == s[-1]:
            print('Working on string: ', s)
            palindrome(s[1:-1])
            return 'Is palindrome'
        else:
            return 'Is not palindrome'

print(palindrome('kayak'))