from random import choices
from sys import argv
# from utility import time_it


def read_file_words(file_name):
    """Returns a list of words from a file of newline-separated words"""
    with open(file_name, 'r') as f:
        words = f.read().split()

    return words


# @time_it
def sentence(num):
    """Takes a random selection of num words and outputs a 'sentence'"""
    words = read_file_words('/usr/share/dict/words')

    sentence = ""
    word_list = choices(words, k=int(num))

    for word in word_list:
        sentence += word + " "

    return sentence


if __name__ == '__main__':
    num = argv[1]
    print(sentence(num))
