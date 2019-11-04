
import pygame
from pygame.locals import *
from core.gameSection import Menu, GameSection
import json

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('resources/songs/a.mp3')

pygame.mixer.music.play(-1)

menu_back = False
class LoopGameEvents(object):
    
    
    def __init__(self, screen):
        self._game = None
        self._screen = screen
        self._current_display = None

        self._surfaces_to_update = []
        self._menu = Menu(screen)
        self._choice = None
        

    def catch_events(self,event, myfont):
        global menu_back
        if  menu_back == True or self._current_display == None: 
            self._current_display = self._menu
            self._choice = None
            menu_back = False
            self._surfaces_to_update.append(self._current_display.blit_elements())

        self._current_display.blit_elements()

        self._choice = self._current_display.check_events(event)    
        
        if self._choice == 1 or isinstance(self._current_display, GameSection) :
            if isinstance(self._current_display, GameSection):
                 if self._current_display._current_level == None:
                     self._current_display = self._menu
                     self._choice = None
                     menu_back = False
                     self._surfaces_to_update.append(self._current_display.blit_elements())
            else: 
                self._current_display =  GameSection(self._screen)
            self._surfaces_to_update.append(self._current_display.blit_elements())    
        
        if self._choice == 2:
            self._current_display =  Info(self._screen)
            self._surfaces_to_update.append(self._current_display.blit_elements())
        
        if self._choice == 3:
            self._current_display =  Ranking(self._screen)
            self._surfaces_to_update.append(self._current_display.blit_elements())

        if self._choice != None and not type(self._choice) == int:
            if len(self._choice)>1:
                if self._choice[1] == False:
                    pygame.mixer.music.pause()
                else: 
                    pygame.mixer.music.unpause()
        

        return self._surfaces_to_update


class Info(object):
    pygame.font.init() 
    myfont = pygame.font.SysFont('freesans', 25)
    title = pygame.font.SysFont('freesans', 40)
    def __init__(self, screen):
        self._surface = pygame.Surface(screen.get_size())
        self._back = pygame.image.load("resources/images/elements/ponto")
        self._info_text = [
                "Toda a ação do jogo é baseada em opções clicáveis com o ",
                "mouse.",
                "",
                "Você pode escolher itens do menu, realizar decisões e encerrar",
                "o jogo clickando sobre a opção desejada.",
                "",
                "Ao final da última fase você terá acesso a sua pontuação.",
                "",
                "",
                "Para retornar ao menu incial pressione o botão no cante esquerdo",
                "inferior"
        ]
        self._btn_back =  pygame.image.load("resources/images/elements/back.png")
        

    def blit_elements(self):
        
        self._surface.blit(self._back,(0,0))
        self._surface.blit(self.title.render("Instruções", False,(255,255,255)),(280,10,0,0))
        self._surface.blit(self._btn_back,(30,410))
        self.blit_info()
        return self._surface
    
    def check_events(self, event):
        global menu_back
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if self._btn_back.get_rect(left=30,top=410).collidepoint(x, y):
                menu_back = True

    def blit_info(self):
        y_text = 0
        for text in self._info_text:
            self._surface.blit(self.myfont.render(text, False,(255,255,255)),(40,70+y_text,100,100))
            y_text += 30


class Ranking(object):
    myfont = pygame.font.SysFont('freesans', 25)
    title = pygame.font.SysFont('freesans', 40)

    def __init__(self, screen):
        self._surface = pygame.Surface(screen.get_size())
        self._back = pygame.image.load("resources/images/elements/ponto")
        self._btn_back =  pygame.image.load("resources/images/elements/back.png")
    
    def blit_elements(self):
        self._surface.blit(self._back,(0,0))
        self._surface.blit(self._btn_back,(30,410))
        self._surface.blit(self.title.render("Ranking", False,(255,255,255)),(280,10,0,0))
        self.blit_info()
        return self._surface
    
    def check_events(self, event):
        global menu_back
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if self._btn_back.get_rect(left=30,top=410).collidepoint(x, y):
                menu_back = True

    def blit_info(self):
        file = open("properties/ranking.json", "r+")
        json_text = json.load(file)
        y_text = 0
        pos = 1
        for text in json_text:
            if pos>=10: return
            blt = str(pos)+"º   "+text[0]+"         "+ str(text[1])
            self._surface.blit(self.myfont.render(blt, False,(255,255,255)),(100,90+y_text,100,100))
            y_text += 30
            pos +=1
        file.close()

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('Game Name')
    pygame.font.init() 
    myfont = pygame.font.SysFont('freesans', 45)


    background = pygame.Surface(screen.get_size())
    background = background.convert()
    
    screen.blit(background, (0, 0)) 

    loop_events = LoopGameEvents(screen)
    surfaces_blit = [background]
    # Event loop
    while 1:
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            surfaces_blit = loop_events.catch_events(event, myfont)
            
        for surface in surfaces_blit:
            background.blit(surface,(0,0))
       
       

        
        screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(100)

main()



