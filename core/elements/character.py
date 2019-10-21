
from ../moviment import CharacterMoviment as moviment
from ../animation import CharacterAnimation as animation


class Character(object):

    def __init__(self):
        self._name = ""
        self._images = []
        self._used_image = ""
        self._pos = 0
        self._surface = 0
        self._size = ()
        self._width = 0
        self._height = 0
        self._level = None
        self._game = None

    def give_tip(self, level, game):
        pass

    def say_story_phrase(self, level, game):
        pass

    def announce_win(self, level, game):
        pass

    def announce_lost(self, level, game):
        pass
    
    def introduce_game(self, game):
        pass

    def introduce_level(self, level, game):
        pass
    
