import time
from string import punctuation


def time_it(func):
    # Made wth love by Ben <3 - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 1000) + ' ms')
        return result

    return wrapper


def read_file_words(file_name):
    """Returns a list of words from a file of newline-separated words"""
    with open(file_name, 'r') as f:
        words = f.read().split()
        new_words = [word.strip(punctuation) for word in words]

    return new_words
