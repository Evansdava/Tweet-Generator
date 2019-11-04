from python.dictionary_words import read_file_words
from python.utility import time_it
from random import randint


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
    """Converts a dictionary histogram to a list of lists"""
    hist = histogram_dict(text)
    hist_list = [[word, hist[word]] for word in hist]

    return hist_list


@time_it
def histogram_dict_tup(text):
    """Converts a dictionary histogram to a list of lists"""
    hist = histogram_dict(text)
    hist_tup = [(word, hist[word]) for word in hist]

    return hist_tup


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


def histogram_counts(text):
    """Create a histogram that groups words by number of occurences"""
    hist = histogram_dict(text)
    values = sorted(hist.values())
    vals = set(values)
    new_hist = []
    for val in vals:
        words = []
        for key in hist:
            if hist[key] == val:
                words.append(key)
        new_hist.append((val, words))

    return new_hist


def swap(swap_list, ind_a, ind_b):
    """Helper function to swap two elements in a list"""
    hold = swap_list[ind_a]
    swap_list[ind_a] = swap_list[ind_b]
    swap_list[ind_b] = hold


def quicksort(histogram, low, high):
    """Sorts a count histogram from lowest number of occurences to highest"""
    if low < high:
        # Partition index
        pi = partition(histogram, low, high)

        # Sort the lower half (below initial pivot)
        quicksort(histogram, 0, pi - 1)

        # Sort the upper half (above initial pivot)
        quicksort(histogram, pi + 1, high)

    return(histogram)


def partition(histogram, low, high):
    """Places smaller elements before a pivot and larger after"""
    # Counter to start from the bottom
    i = low - 1
    # Pivot is the last element of the array
    pivot = histogram[high][0]

    # Iterate through the indices and sort around the pivot
    for j in range(low, high):
        if histogram[j][0] <= pivot:
            i += 1
            swap(histogram, i, j)
    swap(histogram, i + 1, high)
    return i + 1


def unique_words(histogram):
    """Return the number of unique words in a histogram"""
    return len(histogram)


def total_words(histogram):
    """Return the total number of words in a histogram"""
    return sum(histogram.values())


def frequency(histogram, word):
    """Returns the number of times a word appears in a histogram"""
    try:
        return histogram[word]
    except KeyError:
        return "Word not found"


@time_it
def sample_by_dict_freq(histogram):
    """Return a random word, with a probability based on occurences"""
    count = randint(1, total_words(histogram))
    for key in histogram:
        count -= histogram[key]
        if count <= 0:
            return key
    return -1


def sample_by_frequency(histogram):
    """Return a random word with a probability based on occurences

    Works with list of lists and list of tuples
    """
    count = 0
    for word in histogram:
        count += word[1]

    count = randint(1, count)
    for word in histogram:
        count -= word[1]
        if count <= 0:
            return word[0]
    return -1


def generate_sentence(histogram, length):
    """Generate a number of words equal to length and output a 'sentence'"""
    output = ""
    for i in range(length):
        if histogram == list(histogram):
            if i == 0:
                output += sample_by_frequency(histogram).capitalize() + " "
            else:
                output += sample_by_frequency(histogram) + " "
        else:
            if i == 0:
                output += sample_by_dict_freq(histogram).capitalize() + " "
            else:
                output += sample_by_dict_freq(histogram) + " "
    return output


@time_it
def test_sample_freq(histogram, iterations):
    """Test the sample_by_frequency function to ensure randomness"""
    output = []
    for _ in range(iterations):
        sample = sample_by_frequency(histogram)
        assert sample != -1, "Function did not return word"
        output.append(sample)

    return histogram_dict(output)


def run_file(num):
    """Runs everything required, for use in other files"""
    text = read_file_words('python/Iliad.txt')
    # text = "One fish two fish red Fish blue fish".split()
    hist = histogram_dict_tup(text)
    return generate_sentence(hist, num)


if __name__ == '__main__':
    text = read_file_words('Iliad.txt')
    # text = "One fish two fish red Fish blue fish".split()
    hist = histogram_dict_tup(text)
    print(generate_sentence(hist, 10))
