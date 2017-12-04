from src.chipe_utils import *
from src.input_data import *


def decrypt_with_frequency_analyses(cryptogram):
    cryptogram = cleanCryptogram(cryptogram)
    decrypted_messages = []
    for (key, value) in compute_letter_frequency(cryptogram):
        for englishLetter in englishLettersOrderedByFrequency:
            decrypted_message = get_decrypted_message(cryptogram, ord(key) - ord(englishLetter))
            decrypted_messages.append(decrypted_message)
            if decrypted_message.accuracy == cryptogram.split(" ").__len__():
                return sorted(decrypted_messages, key=operator.itemgetter(2), reverse=True)
    return sorted(decrypted_messages, key=operator.itemgetter(2), reverse=True)


def decrypt_with_dictionary_hack(cryptogram):
    cryptogram = cleanCryptogram(cryptogram)
    decrypted_messages = []
    for i in range(0, 26):
        decrypted_message = get_decrypted_message(cryptogram, -i)
        decrypted_messages.append(decrypted_message)
        if decrypted_message.accuracy == cryptogram.split(" ").__len__():
            return sorted(decrypted_messages, key=operator.itemgetter(2), reverse=True)
    return sorted(decrypted_messages, key=operator.itemgetter(2), reverse=True)


decryptions = decrypt_with_frequency_analyses(cryptogram_3)
print("Key:{key} \nMessage: {content}".format(key=decryptions[0].key, content=decryptions[0].content))