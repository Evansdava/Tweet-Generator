try:
    from dictogram import Dictogram
    from utility import read_file_words, time_it
    from queue import Queue
except ImportError:
    from scripts.dictogram import Dictogram
    from scripts.utility import read_file_words, time_it
    from scripts.queue import Queue

# from ast import literal_eval
from random import choice
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


class Markov():
    """A class for generating markov chains and walking through them"""

    def __init__(self, word_file):
        """Initilize starting variables"""
        self.word_list = read_file_words(word_file)
        self.markov = self.make_chain(self.word_list)

    def make_chain(self, word_list):
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

    def walk(self, length):
        """Randomly walk down a markov chain to generate a sentence"""
        output = []
        output.append(choice(tuple(self.markov.keys())))
        for i in range(length):
            output.append(self.markov[output[i]].sample())

        string = ""
        for word in output:
            string += word + " "

        return string


class MarkovN(Markov):
    """A Markov chain of the nth order"""

    def __init__(self, word_file, n):
        """Initialize starting values"""
        self.n = n
        self.word_list = read_file_words(word_file)
        self.markov = self.make_chain(self.word_list)
        # self.store_chain()
        # self.markov = self.retrieve_chain()
        # print(self.markov)

    # def store_chain(self):
    #     """Generates a text file with the Markov Chain info"""
    #     with open('scripts/text/markov_chain_' + str(self.n), "w") as f:
    #         # metadata = f"Corpus Length: {len(self.word_list)} n: {self.n}\n"
    #         # f.write(metadata)
    #         for key, value in self.markov.items():
    #             f.write(f"{key}[:]{(tuple(value.keys()), tuple(value.values()))}\n")

    # @time_it
    # def retrieve_chain(self):
    #     """Retrieves a Markov Chain from a text file"""
    #     markov = {}
    #     with open('scripts/text/markov_chain_' + str(self.n), 'r') as f:
    #         entries = f.readlines()
    #         for entry in entries:
    #             item = entry.split("[:]", 1)
    #             key = item[0]
    #             value = tuple(item[1])
    #             markov[key] = Dictogram(value)

    #     return markov

    # @time_it
    def make_chain(self, word_list):
        """Create and return a markov chain from a given list of words"""
        markov = {}
        q = Queue()
        for i in range(len(word_list)):
            if i < self.n:
                q.enqueue(word_list[i])
            else:
                key = str(q)
                q.dequeue()
                q.enqueue(word_list[i])
                if markov.get(key) is None:
                    markov[key] = []
                markov[key].append(str(q))

        for key in markov:
            markov[key] = Dictogram(markov[key])

        return markov

    # @time_it
    def walk(self, length=0, ends=0):
        """Randomly walk down a markov chain to generate a sentence"""
        output = []
        output.append(choice(tuple(self.markov.keys())))

        # Start token should be a start token
        while output[0].find("[S]") != 0:
            output[0] = choice(tuple(self.markov.keys()))

        output[0] = output[0]
        # Tracking end tokens
        tokens = 0
        i = 0
        while tokens < ends:  # or i < length:
            try:
                next_set = self.markov[output[i]].sample()
                last = next_set[len(next_set) - 3:len(next_set)]
                if last == "[E]":
                    tokens += 1
                output.append(next_set)
                i += 1
            except KeyError:
                break

        string = ""
        for word in output:
            if output.index(word) == 0:
                string += word.replace("[S]", "").replace("[E]", "") + " "
            else:
                try:
                    text = word.split()[-1].replace("[S]", "")
                    string += text.replace("[E]", "") + " "
                except KeyError:
                    return string

        return string


# @time_it
# def markov_chain(word_list):
#     """Create and return a markov chain from a list of words"""
#     markov = {}
#     for i in range(len(word_list)):
#         if word_list[i] not in markov:
#             markov[word_list[i]] = []
#         if i < len(word_list) - 1:
#             markov[word_list[i]].append(word_list[i + 1])

#     for key in markov:
#         markov[key] = Dictogram(markov[key])

#     return markov


# @time_it
# def markov_walk(chain, length):
#     """Randomly walk down a markov chain to generate a sentence"""
#     output = []
#     output.append(choice(tuple(chain.keys())))
#     for i in range(length):
#         output.append(chain[output[i]].sample())

#     string = ""
#     for word in output:
#         string += word + " "

#     return string


def test_markov_n():
    print("Test init:")
    mark = MarkovN('example.txt', 2)
    assert mark.n == 2
    assert mark.word_list == ['one', 'fish', 'two', 'fish',
                              'red', 'fish', 'blue', 'fish']
    print(mark.markov)
    assert mark.markov == {
        "one fish": {"fish two": 1},
        "fish two": {"two fish": 1},
        "two fish": {"fish red": 1},
        "fish red": {"red fish": 1},
        "red fish": {"fish blue": 1},
        "fish blue": {"blue fish": 1}
        }
    print("Init successful")

    print("\nTest make_chain():")
    mark.markov = mark.make_chain("i like cats and you like cats i like dogs \
but you hate dogs".split())
    print(mark.markov)
    assert mark.markov == {
        'i like': {'like cats': 1, 'like dogs': 1},
        'like cats': {'cats and': 1, 'cats i': 1},
        'cats and': {'and you': 1},
        'and you': {'you like': 1},
        'you like': {'like cats': 1},
        'cats i': {'i like': 1},
        'like dogs': {'dogs but': 1},
        'dogs but': {'but you': 1},
        'but you': {'you hate': 1},
        'you hate': {'hate dogs': 1}
        }
    print("\nTesting walk:")
    print(mark.walk(15))


def main(n, num):
    # text = read_file_words('scripts/text_Pride_and_Prej.txt')
    # text = "one fish two fish red fish blue fish".split()
    # text = ('how much wood would a wood chuck chuck'
    #         ' if a wood chuck could chuck wood').split()
    markov = MarkovN('scripts/text/text_Wheel_of_Time_NoNL_S&E.txt', n)

    return markov.walk(ends=num)


if __name__ == '__main__':
    from sys import argv
    num = int(argv[2])
    n = int(argv[1])
    print(main(n, num))
