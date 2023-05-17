import re


def is_palindrome(sentence):
    return sentence[::-1].casefold() == sentence.casefold()


def palindrome_sentence(sentence):
    cleaned_sentence = re.sub("[^a-zA-Z0-9]", '', sentence.lower())
    return is_palindrome(cleaned_sentence)


print(palindrome_sentence("A man, a plan, a canal, Panama!"))  # True


def multipy(a, b):
    result = a * b


print(multipy(4, 5))
