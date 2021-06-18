class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return 'self.text: ' + self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'


if __name__ == '__main__':
    first = Word('ha')
    second = Word('HA')
    third = Word('eh')
    print("'ha' == 'HA'?", first == second)
    print("'ha' == 'eh'?", first == third, end="\n"*2)

    print(first)
