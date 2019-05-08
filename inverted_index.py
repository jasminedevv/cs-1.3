class InvertedIndex(dict):
    def __init__(self, words=None):
        super().__init__() # initialize as dict subclass
        if words is not None:
            for index, word in enumerate(words):
                self.add_index(word, index)
    def add_index(self, word, index):
        try:
            self[word].append(index)
        except KeyError:
            self[word] = [index]

if __name__ == "__main__":
    corpus = "one fish two fish red fish blue fish"
    words = corpus.split()
    my_index = InvertedIndex(words)
    print(my_index)