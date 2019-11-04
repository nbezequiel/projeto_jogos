
import pygame
from pygame.locals import *
from .level import BuildLevels
import sys
import json
import time



class GameSection(object):
    pygame.font.init() 
    infoFont = pygame.font.SysFont('freesans', 25)
    myfont = pygame.font.SysFont('freesans', 45)
    myfont2 = pygame.font.SysFont('freesans', 50)
    title = pygame.font.SysFont('freesans', 40)
    ft = pygame.font.SysFont('freesans', 30)
    @classmethod
    def set_levels(cls):
        pass

    def __init__(self, screen):
        self._surface = pygame.Surface(screen.get_size())
        self._levels = BuildLevels.get_levels(self._surface)
        self._current_level = 0
        self._jogador = ""
        self._pontuacao = 0
        self._data = None
        self._game_music = None
        self._init_game = True
        self._init_name = True
        self._start_game = None
        self._btn_back =  pygame.image.load("resources/images/elements/back.png")
        self._name_game =  None
        self._end_game = False
        self._back_rank = None
        self._myfont = pygame.font.SysFont('freesans', 25)
        self._back = pygame.image.load("resources/images/elements/ponto")
        self._info_text = [
                "    A Vida Cogente de Ubaldo se passa numa cidade fictícia",
                "chamada Turingville, mais especificamente no distrito de", 
                "SãoLinux, onde Ubaldo Javal, o protagonista, vive com sua",
                "família.",
                "   Grande apreciador da lógica e da tecnologia, Ubaldo tende a",
                "enxergar as tarefas mais simples do dia-a-dia como se estivesse",
                "dentro de um grande algoritmo. Para ele, tarefas simples são funções,",
                "decisões são estruturas condicionais, repetições são loops.",
                "O garoto estuda para ser um dia um grande programador e ajudar",
                "a resolver uma boa parcela dos problemas que lhe cercam, porém,",
                "todo dia se defronta com seu maior inimigo, o tempo."
        ]
        
 
    def change_level(self):
        if self._levels[self._current_level] != None:
            if self._levels[self._current_level]._completed == True: 
                if self._current_level < 5:
                    self._current_level += 1
        
            
    def blit_info(self):
        y_text = 0
        for text in self._info_text:
            self._surface.blit(self.infoFont.render(text, False,(255,255,255)),(40,90+y_text,100,100))
            y_text += 30         
    

    def blit_elements(self):
        back = pygame.image.load("resources/images/elements/ponto")
        self._surface.blit(back, (0,0))
        self._name_game = pygame.image.load("resources/images/elements/proximo.png")
        self._surface.blit(self._name_game,(700,410))

        self._surface.blit(self.myfont2.render(self._jogador, False,(255,255,255)), (280,150, 100, 40))
        self._surface.blit(self.myfont.render("Digite o seu nome: ", False,(255,255,255)), (250,50, 100, 40))
        
        if self._init_name == True: return self._surface

        self._surface.blit(back, (0,0))
        self._start_game = pygame.image.load("resources/images/elements/proximo.png")
        self._surface.blit(self._start_game,(700,410))
        self._surface.blit(self.title.render("A Vida Cogente de Ubaldo", False,(255,255,255)),(230,10,0,0))
        self.blit_info()
        if self._init_game == True: return self._surface

        self.change_level()
        if self._levels[self._current_level] != None:
            self._levels[self._current_level].blit_elements()
        else:
            self._back_rank = pygame.image.load("resources/images/elements/ponto")
            self._surface.blit(self._back_rank, (0,0))
            self.blit_ranking()

        return self._surface
    
    def takeSecond(elem):
        return elem[1]
    def blit_ranking(self):
        self._surface.blit(self._btn_back,(30,410))
        if not self._end_game:
            self.get_pontuacao()
            file = open("properties/ranking.json", "r+")
            json_text = json.load(file)
            json_text.append([self._jogador,self._pontuacao])
            json_text.sort(reverse = True,key = lambda lem: lem[1])
            file.close()
            file = open("properties/ranking.json", "w")
            
            json.dump(json_text,file)
            file.close()
            self._end_game =True
        self._surface.blit(self.title.render("Ranking", False,(255,255,255)),(280,10,0,0))
        
        self._surface.blit(self.ft.render("Sua pontuação: "+str(self._pontuacao), False,(255,255,255)),(450,60,0,0))
        
        file = open("properties/ranking.json", "r+")
        json_text = json.load(file)
        file.close()
        y_text = 0
        pos = 1
        for text in json_text:
            if pos == 10: return
            blt = str(pos)+"º   "+text[0]+"         "+ str(text[1])
            self._surface.blit(self._myfont.render(blt, False,(255,255,255)),(100,90+y_text,100,100))
            y_text += 30
            pos +=1
        
        


    def check_events(self, event):
        
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                if self._btn_back.get_rect(left=30,top=410).collidepoint(x, y):
                    self._current_level = None
            if self._name_game.get_rect(left=700,top=410).collidepoint(x, y):
                self._init_name = False
            if self._start_game != None:
                if self._start_game.get_rect(left=700,top=410).collidepoint(x, y):
                    self._init_game = False
                    if self._jogador == "":
                        self._jogador = "Noname"
        
        if self._current_level != None:
            if self._levels[self._current_level] != None:    
                self._levels[self._current_level].check_events(event)
        
        
        if self._init_name == True: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(self._jogador)
                    self._jogador = ''
                elif event.key == pygame.K_BACKSPACE:
                    self._jogador = self._jogador[:-1]
                else:
                    if len(self._jogador ) <= 13:
                        self._jogador += event.unicode
                        print(self._jogador)
                        

                
                
                    
        
    

    def get_pontuacao(self):
        for level in self._levels:
            if level != None:
                self._pontuacao += level.get_score(level._problem)


class Menu(object):
    pygame.font.init() 
    myfont = pygame.font.SysFont('freesans', 40)
    title = pygame.font.SysFont('freesans', 40)
    def __init__(self, screen):
        self._game_title = ""
        self._message = ""
        self._menu_options = [
            {"mensagem":"Jogar"},
            {"mensagem":"Instruções"},
            {"mensagem":"Ranking"},
            {"mensagem":"Sair"}]
        self._sound = True
            
        self._surface = pygame.Surface(screen.get_size())
        self._buttons = []
        self._BUTTON_COLOR = (0,255,255)
        
    def blit_elements(self):
        back_image = pygame.image.load("resources/images/elements/ponto")
        self._surface.blit(back_image,(0,0))
        self._surface.blit(self.title.render("A Vida Cogente de Ubaldo", False,(0,0,0)),(170,10,0,0))
        rect1 = pygame.Rect((350,160),(10, 10)) 
        self._buttons.append(pygame.image.load("resources/images/elements/blue_rec.png")) 
        self._buttons.append(pygame.image.load("resources/images/elements/blue_rec.png"))   
        self._buttons.append(pygame.image.load("resources/images/elements/blue_rec.png"))   
        self._buttons.append(pygame.image.load("resources/images/elements/blue_rec.png"))   
        self._buttons.append(pygame.image.load("resources/images/Misc/Config/Sound.png"))


        self._surface.blit(self._buttons[0],(250,180))
        self._surface.blit(self._buttons[1],(250,240))
        self._surface.blit(self._buttons[2],(250,300))
        self._surface.blit(self._buttons[3],(250,360)) 
        self._surface.blit(self._buttons[4],(40,410))



        self._surface.blit(self.myfont.render(self._menu_options[0]["mensagem"], False,(0,0,0)), (340,186, 100, 40))
        self._surface.blit(self.myfont.render(self._menu_options[1]["mensagem"], False,(0,0,0)), (300,245, 100, 40))
        self._surface.blit(self.myfont.render(self._menu_options[2]["mensagem"], False,(0,0,0)), (320,310, 100, 40))
        self._surface.blit(self.myfont.render(self._menu_options[3]["mensagem"], False,(0,0,0)), (350,368, 100, 40))
        
        return self._surface
    
    def check_events(self, event):
        
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if self._buttons[0].get_rect(left=250,top=180).collidepoint(x, y):
                return 1
            
            if self._buttons[1].get_rect(left=250,top=240).collidepoint(x, y):
                return 2
            
            if self._buttons[2].get_rect(left=250,top=300).collidepoint(x, y):
                return 3

            if self._buttons[4].get_rect(left=40,top=410).collidepoint(x, y):
                if self._sound:
                    self._buttons[4] = pygame.image.load("resources/images/Misc/Config/NoSound.png")
                    self._sound = False
                else:
                    self._buttons[4] = pygame.image.load("resources/images/Misc/Config/Sound.png")
                    self._sound = True
                return 4,self._sound
            
            if self._buttons[3].get_rect(left=250,top=360).collidepoint(x, y):
                sys.exit(0)
            


