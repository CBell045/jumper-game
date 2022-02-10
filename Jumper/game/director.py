from game.choose_word import Call_word
from game.jumper import Jumper

class Director:
    def __init__(self) -> None:
        self._is_playing = True
        self._score = 0
        self._jumper = Jumper()
        self._word = Call_word()


    def start_game(self):
        self._word._choose_random_word()
        self._word._create_blank_word()
        self._jumper._print_jumper(self._score)
        self._word.print_current_word()
        while self._is_playing == True:
            self._get_inputs()
            self._do_outputs()

    def _get_inputs(self):
        guess =  str(input("Type a letter: "))
        if not self._word.check_guess(guess):
            self._score += 1
        if self._score > 3:
            print(f"Sorry, you lost. The word was {self._word._split_word}") 
            self._is_playing = False
        elif self._word._current_word == self._word._split_word:
            print("You won!")
            self._is_playing = False

    def _do_outputs(self):
        self._word.print_current_word()
        self._jumper._print_jumper(self._score)