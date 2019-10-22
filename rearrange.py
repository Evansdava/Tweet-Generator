from random import choice
from sys import argv


def rearrange(words):
    """Take a list of words and rearrange them, returning a new list"""
    word_list = []
    while words != []:
        next_word = choice(words)
        word_list.append(next_word)
        words.remove(next_word)

    return word_list


if __name__ == '__main__':
    words = argv[1:]
    print(words)
    word_list = rearrange(words)
    for word in word_list:
        print(word, end=' ')
