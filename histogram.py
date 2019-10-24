from dictionary_words import read_file_words


def histogram(text):
    """Read a text and return a histogram of its words"""
    hist = {}
    for word in text:
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1
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
    print(frequency(histogram(text), 'Apollo'))
