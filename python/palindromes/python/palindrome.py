import re


def palindrome(word):
    # Make sure it's a string and all letters are lowercase.
    stringify = str(word).lower()
    # Remove special characters and whitespace
    forward = str(re.sub("[^A-Za-z0-9]+", "", stringify))
    # Reverse the string
    backwards = forward[::-1]

    return True if forward == backwards else False
