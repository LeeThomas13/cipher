import re
from corpus_loader import name_list, word_list

def count_words(text):

    candidates = text.split()

    word_count = 0

    for promising in candidates:
        potential_words = re.sub(r'[^A-Za-z]+', '', promising)

        if potential_words.lower() in word_list or potential_words in name_list:
            word_count += 1

        return word_count


count_words('a dark and stormy night 1234%%%^&&')