
import pygame
from pygame.locals import *
from .level import BuildLevels
import sys

class GameSection(object):

    @classmethod
    def set_levels(cls):
        pass

    def __init__(self, screen):
        self._surface = pygame.Surface(screen.get_size())
        self._levels = BuildLevels.get_levels(self._surface)
        self._current_level = 0
        self._jogador = None
        self._pontuacao = 0
        self._data = None
        self._game_music = None
        

    def change_level(self):
        if self._levels[self._current_level]._completed == True: 
            self._current_level += 1
            self._current_level = self._levels[self._current_level]
    

    def blit_elements(self):
        self.change_level()
        self._levels[self._current_level].blit_elements()
        return self._surface

    def check_events(self, event):
        self._levels[self._current_level].check_events(event)


class Menu(object):


    def __init__(self, screen):
        self._game_title = ""
        self._message = ""
        self._menu_options = [
            {"mensagem":"Jogar"},
            {"mensagem":"Instruções"},
            {"mensagem":"Ranking"},
            {"mensagem":"Sair"}]
            
        self._surface = pygame.Surface(screen.get_size())
        self._buttons = []
        self._BUTTON_COLOR = (0,255,255)
        
    def blit_elements(self, events, myfont):
        self._surface.fill((255,255,255))
        rect1 = pygame.Rect((350,160),(10, 10))        
        self._buttons.append(pygame.draw.rect(self._surface,self._BUTTON_COLOR,(290,160,230,50)))
        
        rect2 = pygame.Rect((313,220),(10, 10))
        self._buttons.append(pygame.draw.rect(self._surface,self._BUTTON_COLOR,(290,220,230,50)))
        
        rect3 = pygame.Rect((328,280),(10, 10))
        self._buttons.append(pygame.draw.rect(self._surface,self._BUTTON_COLOR,(290,280,230,50)))

        
        rect4 = pygame.Rect((365,340),(10, 10))
        self._buttons.append(pygame.draw.rect(self._surface,self._BUTTON_COLOR,(290,340,230,50)))



        self._surface.blit(myfont.render(self._menu_options[0]["mensagem"], False,(0,0,0)), rect1)
        self._surface.blit(myfont.render(self._menu_options[1]["mensagem"], False,(0,0,0)), rect2)
        self._surface.blit(myfont.render(self._menu_options[2]["mensagem"], False,(0,0,0)), rect3)
        self._surface.blit(myfont.render(self._menu_options[3]["mensagem"], False,(0,0,0)), rect4)
        
        return self._surface
    
    def check_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if self._buttons[0].collidepoint(x, y):
                return 1
            
            if self._buttons[1].collidepoint(x, y):
                return 2
            
            if self._buttons[2].collidepoint(x, y):
                return 3
            
            if self._buttons[3].collidepoint(x, y):
                sys.exit(0)
            


