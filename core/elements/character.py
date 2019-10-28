
from ..moviment import CharacterMoviment as moviment
from ..animation import CharacterAnimation as animation

class Character(object):

    def __init__(self):
        self._images = []
        self._used_image = ""
        self._speaking = False
        self._pos = 0
        self._surface = 0
        self._size = ()
        self._width = 0
        self._height = 0
        self._message = None
        self._text_baloon = None ## classe com imagem de fundo e texto dinâmico posição de personagem calculada

    def speak(self):
        self._speaking = True



class Compilador(Character):

    def __init__(self):
        super().__init__(self)

    def give_tip(self, level, game):
        pass

    def announce_win(self, level, game):
        pass

    def announce_lost(self, level, game):
        pass
    
    def introduce_game(self, game):
        pass

    def introduce_level(self, level, game):
        pass
    
    ### finaliza jogo
    ### 
    
