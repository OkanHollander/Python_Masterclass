import re


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string

    return string[::-1].casefold() == string.casefold()


print(is_palindrome("Lol"))
print(is_palindrome("RaDar"))


def palindrome_sentence(string):
    cleaned_sentence = re.sub('[^a-zA-Z0-9]', '', string.lower())
    return cleaned_sentence == cleaned_sentence[::-1]


print(palindrome_sentence("A man, a plan, a canal, Panama!"))  # True
print(palindrome_sentence("Madam, in Eden, I'm Adam."))  # True
print(palindrome_sentence("Hello, world!"))  # False
