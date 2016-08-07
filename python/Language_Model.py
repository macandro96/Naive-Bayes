import math

class Language_Model(object):
    def __init__(self):
        self.word_database = {}
        self.counter = 0

    def add_word(self, word):
        if self.word_database.get(word) is None:
            self.word_database[word] = 1

        else:
            count = self.word_database[word]
            self.word_database[word] = count + 1

        self.counter += 1

    def get_count(self, word):
        if self.word_database.get(word) is None:
            return 0
        return self.word_database[word]

    def is_Unknown(self, word):
        return self.get_count(word) == 0

    def get_probability(self, word, vocabulary):
        if self.is_Unknown(word):
            return float((self.get_count(word) + 1.0 )/ (self.counter + vocabulary + 1))
        else:
            return float((self.get_count(word) + 1.0 )/ (self.counter + vocabulary))

    def getLogProbability(self, word, vocabulary):
        return math.log10(self.get_probability(word, vocabulary))








