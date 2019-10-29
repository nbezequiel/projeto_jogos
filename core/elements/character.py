import pygame
from ..moviment import CharacterMoviment as moviment
from ..animation import CharacterAnimation as animation
from .geo_figures import GeoFigures

pygame.display.set_caption('Game Name')
pygame.font.init() 
myfont = pygame.font.SysFont('loma', 12)

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



class Compilador(object):

    def __init__(self, surface, pos, message):
        self._main_image = pygame.image.load("resources/images/elements/compilador1.png")
        self._images = [pygame.image.load("resources/images/elements/compilador1.png"), pygame.image.load("resources/images/elements/compilador3.png")]
        self._size = (100,40)
        self._pos = pos
        self._speaking = True
        self._message = message
        self._surface = surface
        self._message_pos =(self._pos[0]-20, self._pos[1] -30, 300, 300)
        self._text_baloon = None
        

    def blit_elements(self, surface):
        surface.blit(self._main_image, self._pos)
        self.blit_message(self._message, surface)
        
    def change_baloon_size(self, new_size):
        self._message_pos = new_size
        self._text_baloon = GeoFigures().get_rectangle(self._surface,(255,255,255), new_size)

    def blit_message(self, message, surface):
        y_text= 0
        if self._speaking:
            self._text_baloon = GeoFigures().get_rectangle(surface,(255,255,255), (self._pos[0]-20, self._pos[1] -30, 300, 300))
            for  text in message:
                pos = self._message_pos
                surface.blit(myfont.render(text, False,(0,0,0)),( pos[0],pos[1]+ y_text, pos[2], pos[3]))
                y_text += 13

    def give_tip(self, level, game, message):
        self.blit_message(message)


    def announce_win(self, level, game, message):
        self.blit_message(message)

    def announce_lost(self, level, game, message):
        self.blit_message(message)
    
    def introduce_game(self, game, message):
        self.blit_message(message)

    def introduce_level(self, level, game, message):
        self.blit_message(message)
    
    
    def end_game(self, level, game, message):
        self.blit_message(message) 
    
