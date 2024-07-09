# 4. String Length: Write a recursive function to find the length of a string

def string_length(s):
    if len(s) == 0:
        return 0
    else:
        return 1 + len(s[:-1])



print(string_length('hello, brubru!'))