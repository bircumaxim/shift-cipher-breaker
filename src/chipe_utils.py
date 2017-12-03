import operator
import string
from collections import namedtuple
import enchant
import re

dictionary = enchant.Dict("en-US")
DecryptedMessage = namedtuple("DecryptedMessage", ["content", "key", "accuracy"])

englishLettersOrderedByFrequency = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "i", "c", "u", "m", "w", "f", "g",
                                    "y", "p", "b", "v", "k", "j", "x", "q", "z"]


def shift(text, key):
    data = ""
    for letter in text:
        if letter != ' ':
            data += get_shifted_char(letter, key)
        else:
            data += letter
    return data


def get_shifted_char(c, shift):
    new_position = ord(c) + shift
    if new_position > ord('z'):
        new_position = ord('a') + new_position - ord('z') - 1
    if new_position < ord('a'):
        new_position = ord('z') - (ord('a') - new_position) + 1
    return chr(new_position)


def compute_letter_frequency(text):
    frequency = {}
    for letter in text.replace(" ", ""):
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)


def get_decrypted_message(text, key):
    content = shift(text, key)
    accuracy = 0
    for word in (content.split()):
        if dictionary.check(word): accuracy += 1
    return DecryptedMessage(content, key, accuracy)


def cleanCryptogram(cryptogram):
    return re.sub(r'[^\w\s]', '', cryptogram.lower())
