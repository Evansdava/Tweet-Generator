from random import choices
from sys import argv


def sentence(num):
    """Takes a random selection of num words and outputs a 'sentence'"""
    f = open('/usr/share/dict/words', 'r')
    words = f.readlines()
    sentence = ""
    word_list = choices(words, k=int(num))
    for word in word_list:
        sentence += word.strip() + " "
    f.close()
    return sentence


if __name__ == '__main__':
    num = argv[1]
    print(sentence(num), end=" ")
