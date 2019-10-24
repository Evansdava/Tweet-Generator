from random import randint  # , choice
from sys import argv
from math import factorial
from utility import time_it


def shuffle(obj):
    """Take an object (list or string) and shuffle the elements"""
    if obj == str(obj):
        string = True
    else:
        string = False

    obj = list(obj)
    num = len(obj)
    while num:
        num -= 1
        rand = randint(0, num)
        hold = obj[num]
        obj[num] = obj[rand]
        obj[rand] = hold

    if string:
        obj = ''.join(obj)

    return obj


@time_it
def rearrange(words):
    """Take a list of words and rearrange them, returning a new list"""
    # Fisher-Yates style:
    shuffle(words)
    return words

    # Less optimal
    # word_list = []
    # while words != []:
    #     next_word = choice(words)
    #     word_list.append(next_word)
    #     words.remove(next_word)

    # return word_list


@time_it
def anagrams(word):
    """Take a word and return a set of anagrams for it"""
    perm_num = factorial(len(word))
    anagram_set = set()
    count = 0
    while count < perm_num:
        if word not in anagram_set:
            anagram_set.add(word)
            count += 1
        word = shuffle(word)

    return anagram_set


if __name__ == '__main__':
    # words = argv[1:]
    # word_list = rearrange(words)

    # for word in word_list:
    #     print(word, end=' ')

    word = argv[1]
    anagrams(word)
