from dictionary_words import read_file_words
from utility import time_it


@time_it
def histogram(text):
    """Read a text and return a histogram of its words"""
    # Dictionary
    hist = {}
    for word in text:
        word = word.lower()
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1

    # List of lists
    # hist = []
    # added = True
    # for word in text:
    #     word = word.lower()
    #     for word_list in hist:
    #         if word_list[0] == word:
    #             word_list[1] += 1
    #             added = False
    #     if added is True:
    #         hist.append([word, 1])
    #     added = True

    # List of tuples
    # hist = []
    # added = True
    # for word in text:
    #     word = word.lower()
    #     for word_tup in hist:
    #         if word_tup[0] == word:
    #             word_list = list(word_tup)
    #             word_list[1] += 1
    #             hist[hist.index(word_tup)] = tuple(word_list)
    #             added = False
    #     if added is True:
    #         hist.append((word, 1))
    #     added = True

    return hist


def unique_words(histogram):
    """Return the number of unique words in a histogram"""
    return len(histogram)


def total_words(histogram):
    """Return the total number of words in a histogram"""
    total = 0
    for word in histogram:
        total += histogram[word]
    return total


def frequency(histogram, word):
    """Returns the number of times a word appears in a histogram"""
    return histogram[word]


if __name__ == '__main__':
    text = read_file_words('Iliad.txt')
    text = "One fish two fish red fish blue fish".split()
    print(histogram(text))
