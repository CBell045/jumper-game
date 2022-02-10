import random as ram

class Call_word:

    def __init__(self):
        self._words = ['cool' , 'jump']
        self._split_word = []
        self._current_word = []

    def print_current_word(self):
        print(self._current_word)

    def _choose_random_word(self):
        self._split_word = list(self._words[ram.randint(0,len(self._words)-1)])
        return self._split_word
        
    def _create_blank_word(self):
        self._current_word = ["_" for i in range(len(self._split_word))]
        return self._current_word

    def check_guess(self, guess):
        if guess in self._split_word:
            for i in range(0, len(self._split_word)):
                if self._split_word[i] == guess:
                    self._current_word[i] = guess
            return True
        return False