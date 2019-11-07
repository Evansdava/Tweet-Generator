from scripts.dictogram import Dictogram
from random import choice
from utility import time_it, read_file_words
"""
Read a file, turn it into a list

Declare a data structure to hold information
For each word in the list of words:
    If the word is not already present in the data structure:
        Create an entry for the word (word: list of following words)
    Check the next word in the list
    Add the next word to the list of the current word
Create histograms for each word, and assign them to each entry
"""


@time_it
def markov_chain(word_list):
    """Create and return a markov chain from a list of words"""
    markov = {}
    for i in range(len(word_list)):
        if word_list[i] not in markov:
            markov[word_list[i]] = []
        if i < len(word_list) - 1:
            markov[word_list[i]].append(word_list[i + 1])

    for key in markov:
        markov[key] = Dictogram(markov[key])

    return markov


@time_it
def markov_walk(chain, length):
    """Randomly walk down a markov chain to generate a sentence"""
    output = []
    output.append(choice(tuple(chain.keys())))
    for i in range(length):
        output.append(chain[output[i]].sample())

    string = ""
    for word in output:
        string += word + " "

    return string


def main():
    text = read_file_words('text_Pride_and_Prej.txt')
    # text = "one fish two fish red fish blue fish".split()
    # text = ('how much wood would a wood chuck chuck'
    #         ' if a wood chuck could chuck wood').split()
    print(markov_walk(markov_chain(text), 10))


if __name__ == '__main__':
    main()
