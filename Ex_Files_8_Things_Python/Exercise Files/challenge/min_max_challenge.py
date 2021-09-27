import string
import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# DICTIONARY = 'C:\Users\joeom\Desktop\coding\8thingsLI\Ex_Files_8_Things_Python\Exercise Files\challenge\dictionary.txt'
DICTIONARY = 'dictionary.txt'

letter_scores = {
                    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 
                    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 
                    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 
                    'y': 4, 'z': 10
                }

def get_scrabble_dictionary():
    """Helper function to return the words in DICTIONARY as a list"""
    with open(DICTIONARY, 'rt', encoding='utf-8') as file:
        content = file.read().splitlines()
    return content

def score_word(word):
    """Return the score for a word using letter_scores.
    If the word isn't in DICTIONARY, it gets a score of 0.""" 
    score = 0
    words = get_scrabble_dictionary()
    if word.upper() in words:
        for i in word:
            lowered = i.lower()
            score += letter_scores[lowered]
    return score

def remove_punctuation(word):
    """Helper function to remove punctuation from word"""
    table = str.maketrans({char:None for char in word if char in string.punctuation})
    return word.translate(table)

def get_word(pair):
    word, score = pair
    return word

def get_word_largest_score(sentence):
    """Given a sentence, return the word in the sentence with the largest score."""
    scores = []
    split_sentence = sentence.split()
    nopunct = []
    for i in split_sentence:
        nopunct.append(remove_punctuation(i))
        scores.append(score_word(remove_punctuation(i)))
    return max(zip(scores,nopunct), key=get_word)

    
