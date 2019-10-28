from dictionary_words import read_file_words
from utility import time_it


@time_it
def histogram_dict(text):
    """Read a text and return a dictionary histogram of its words"""
    hist = {}
    for word in text:
        word = word.lower()
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1

    return hist


@time_it
def histogram_dict_list(text):
    hist = histogram_dict(text)
    hist_list = [[word, hist[word]] for word in hist]

    return hist_list


@time_it
def histogram_list(text):
    """Read a text and return a list histogram of its words"""
    hist = []
    added = True
    for word in text:
        word = word.lower()
        for word_list in hist:
            if word_list[0] == word:
                word_list[1] += 1
                added = False
        if added is True:
            hist.append([word, 1])
        added = True

    return hist


@time_it
def histogram_tuple(text):
    """Read a text and return a tuple histogram of its words"""
    hist = []
    added = True
    for word in text:
        word = word.lower()
        for word_tup in hist:
            if word_tup[0] == word:
                word_list = list(word_tup)
                word_list[1] += 1
                hist[hist.index(word_tup)] = tuple(word_list)
                added = False
        if added is True:
            hist.append((word, 1))
        added = True

    return hist


def swap(swap_list, ind_a, ind_b):
    """Helper function to swap two elements in a list"""
    hold = swap_list[ind_a]
    swap_list[ind_a] = swap_list[ind_b]
    swap_list[ind_b] = hold


def sort_by_frequency(histogram, low, high):
    """Sorts a list histogram from highest number of occurences to lowest"""
    # Using quicksort
    if low < high:
        # Partition index
        pi = partition(histogram, low, high)

        # Sort the lower half (below initial pivot)
        sort_by_frequency(histogram, 0, pi - 1)

        # Sort the upper half (above initial pivot)
        sort_by_frequency(histogram, pi + 1, high)

    # return(histogram)


def partition(histogram, low, high):
    """Places smaller elements before a pivot and larger after"""
    # Counter to start from the bottom
    i = low - 1
    # Pivot is the last element of the array
    pivot = histogram[high][1]

    # Iterate through the indices and sort around the pivot
    for j in range(low, high):
        if histogram[j][1] <= pivot:
            i += 1
            swap(histogram, i, j)
    swap(histogram, i + 1, high)
    return i + 1


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
    try:
        return histogram[word]
    except KeyError:
        return "Word not found"


def sample_by_frequency(histogram):
    """Return a random word, with a probability based on occurences"""
    pass


if __name__ == '__main__':
    text = read_file_words('Iliad.txt')
    text = "One fish two fish red Fish blue fish".split()
    text = "three three three two two one".split()
    hist = histogram_dict_list(text)
    print(hist)
    sort_by_frequency(hist, 0, len(hist) - 1)
    print(hist)
