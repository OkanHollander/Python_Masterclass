def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string

    return string[::-1] == string

print(is_palindrome("lol"))
print(is_palindrome("word"))
