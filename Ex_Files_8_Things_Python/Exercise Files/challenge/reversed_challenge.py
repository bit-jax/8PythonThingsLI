import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub('\W+', '', words)

def is_palindrome(words):
    '''Palindromes are case insensitive, so both radar and Radar are valid'''
    return remove_punctuation(words).lower() == remove_punctuation(words).lower()[::-1]
    # if remove_punctuation(words).lower() == remove_punctuation(words).lower()[::-1]:
    #     return True
    # else:
    #     return False