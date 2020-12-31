import re
from corpus_loader import name_list, word_list

def encrypt(plain, shift):
    encrypted_string = ""

    for char in plain:
        num = str(char)
        shifted_num = num + shift
        shifted_num_string = str(shifted_num)
        encrypted_string += shifted_num_string

    return encrypted_string


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)


def verify_words(text):

    candidates = text.split()

    word_count = 0

    for promising in candidates:
        potential_words = re.sub(r'[^A-Za-z]+', '', promising)

        if potential_words.lower() in word_list or potential_words in name_list:
            word_count += 1

        return word_count


def crack_code(encoded):
    # takes in encoded sting
    # sends it to decrypt function, trying shifts of 1-26
    # gets all results from decrypt function and sends them through verify_words function
    # returns the shift result with the highest word confidence value
    pass