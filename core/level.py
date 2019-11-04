import pygame
import sys
import time

sys.path.append("..")
from core.elements.geo_figures import *
from .elements.character import Compilador

pygame.display.set_caption('Game Name')
pygame.font.init() 
myfont = pygame.font.SysFont('freesans', 17)

import threading

#from ..utils.properties_reader import PropertiesReader
from utils.properties_reader import PropertiesReader

from pygame.locals import *
threads = []
class Level(object):

    
    def __init__(self, surface):
        self._surface = surface
        self._score = 0 
        self._characters = []
        self._init_characters = []
        self._end_characters = []
        self.clickable_choices = []
        self._background = None
        self._timer = None ## time progressivo
        self._problem =  Problem()
        self._end_animation =  self.check_animation(self._problem)
        self._init_screen = True
        self._completed = False
        self._next_init_btn = None
        self._next_level_btn = None
        self._printed_pontuation  = False
        

    @property
    def clickable_choices(self):
        return self._clickable_choices

    @clickable_choices.setter
    def clickable_choices(self, clickable_choices):
        self._clickable_choices = clickable_choices

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, characters):
        self._clickable_choices = characters

    def clicked_element(self, event):
        pass

    def check_animation(self, problem):
        pass 


    def get_score(self, problem):
        return self._problem.get_score()



    def blit_elements(self):
        if self._problem._next_level_btn != None and self._printed_pontuation == False:
            self._problem.get_pontuation()
            self._printed_pontuation = True

        if self._init_screen == True:
            self._surface.blit(self._background, (0,0))
            for character in self._init_characters:
                character.blit_elements(self._surface)
            self._next_init_btn = pygame.image.load("resources/images/elements/proximo.png")
            self._surface.blit(self._next_init_btn,(700,410))


        if self._init_screen == True: return self._surface

        self._surface.blit(self._background, (0,0))
        
        self._surface = self._problem.blit_elements(self._surface)
       
        for character in self._characters:
            self._surface.blit(character._main_image)
            if character._speaking == True: 
                self._surface.blit(character._text_baloon)
                self._surface.blit(character._message)
        
        for clickable in self._clickable_choices:
            self._surface.blit(clickable._image)
        
        return self._surface

    def check_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if self._next_init_btn != None and self._init_screen == True:
                global threads
                if self._next_init_btn.get_rect(left=700,top=410).collidepoint(x, y):
                    #global threads
                    #for thr in threads:
                      #  if thr.is_alive():
                       #     thr.join()
                    
                    #def gfg(): 
                   #     num = 0
                    #    while True:
                            
                     #       print("\n",num,"\n") 
                      #      num +=1
                       #     time.sleep(1)
                    
                   # timer = threading.Thread(target = gfg, args=()) 
                    #timer.start()
                    #threads.append(timer)
                    self._init_screen = False
                    

            if self._problem._next_level_btn != None:
                if self._problem._next_level_btn != None and self._init_screen == False:
                    if self._problem._next_level_btn.get_rect(left=700,top=410).collidepoint(x, y):
                        self._completed = True
                        global Next_level_btn
                        Next_level_btn = None
                        print("bbbb")
        self._problem.check_events(event)
        
    def timer_start(self):
        pass

    def start_final_animation(self):
        pass
    
Next_level_btn = None
class Node(object):
    
    btn_yes = None
    btn_no = None
    

    def __init__(self, surface, node_type, pos, text_pos):

        self._node_type = node_type
        self._pos = pos 
        self._text_pos = text_pos
        self._surface = surface
        self._animation_id = None
        self._value = None
        self._text_ballon = None
        self._message = None
        self._type = None
        self._right_node = None
        self._arrow = None
        self._left_node = None
        self._enabled = False
        self._decision = None
        self._btn_yes = None
        self._btn_no = None
        

    def set_pos(self, pos):
        self._pos = pos
        return self

    def with_value(self, value):
        self._value = value
        return self
    
    def with_message(self, message):
        self._message = message
        return self
    
    def set_node_type(self, node_type):
        self._node_type = node_type
        return self
    
    def set_enabled(self, enable):
        self._enabled = enable
        return self

    def get_pontuation(self, node):
        pontuation = 0
        if node._right_node != None:
            if node._right_node._enabled == True: 
                pontuation += node.get_pontuation(node._right_node)
        if node._left_node != None:
            if node._left_node._enabled == True: 
                pontuation += node.get_pontuation(node._left_node)

        return node._value + pontuation      

    def set_text_ballon_format(self):
        
        if self._node_type == 1 or self._node_type == 4  or self._node_type == 5:
            x = GeoFigures()
            return x.get_rectangle(self._surface,(255,255,255), self._pos)
        
        
        if self._node_type == 2:
            x = GeoFigures()
            return x.get_square(self._surface,(255,255,255), self._pos)



    def show(self):
        self._enabled = True 
        pass
    
    def hide(self):
        self._enabled = False
        pass ###esconde tudo dele e filhos

    def check_events(self, event, node):
        if node._right_node != None:
            if node._right_node._enabled == True: 
                node._right_node.check_events(event,node._right_node)
        if node._left_node != None:
            if node._left_node._enabled == True: 
                node._left_node.check_events(event,node._left_node)
        
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if node._btn_yes != None:
                print(x,y)
                if node._btn_yes.convert_alpha().get_rect(left=700, top=200).collidepoint(x, y) and node._right_node != None:
                    node._right_node._enabled = True
                    print("aaaa")
            
            if node._btn_no != None:
                if node._btn_no.convert_alpha().get_rect(left=700, top=255).collidepoint(x, y) and node._left_node != None:
                    node._left_node._enabled = True
                    print("bbb")
        
        return 

    def blit_elements(self, node, surface):
        
        if node == None: return
        if node._enabled == True: 
            last_active_node = node

        if node._node_type == 4 and node._enabled == True : 
            global Next_level_btn
            Next_level_btn = pygame.image.load("resources/images/elements/proximo.png")
            surface.blit(Next_level_btn,(700,410))

        if node._enabled == True and node._node_type != 0: 
            node._text_ballon = node.set_text_ballon_format()
            y_text = 0
            for text in node._message:
                pos = node._text_pos
                surface.blit(myfont.render(text, False,(255,255,255)),(pos[0],pos[1] +y_text, pos[2], pos[3]))
                y_text += 13
            #surface.blit(self._arrow, rect)
        
        if node._right_node != None:
            if node._enabled == True and node._right_node._node_type == 4 or node._right_node._node_type == 2:
                node._right_node._enabled = True
                self.blit_elements(node._right_node, surface)
                
        
        if node._left_node != None :

            if node._enabled == True and node._left_node._node_type == 4 or node._left_node._node_type == 2:
                node._left_node._enabled = True
                self.blit_elements(node._left_node, surface)
                

        if node._right_node != None and node._left_node != None:
            self.blit_elements(node._right_node, surface)
            self.blit_elements(node._left_node, surface)
        
        if node._node_type == 2 and node._left_node._enabled == False and node._right_node._enabled == False:
            node._btn_yes = pygame.image.load("resources/images/elements/sim.png")
            surface.blit(node._btn_yes,(700,200))
            node._btn_no = pygame.image.load("resources/images/elements/nao.png")
            surface.blit(node._btn_no,(700,255))
        
        if Next_level_btn != None and node._node_type == 5:
            return Next_level_btn
        return

    
from functools import reduce
class Problem(object):

    def __init__(self):
        self._root_node = None
        self._animation = None
        self._list_nodes = []
        self._next_level_btn = None


    def get_score(self):
        return self._root_node.get_pontuation(self._root_node)

    def start_animation(self):
        pass

    def blit_elements(self, surface):
        self._next_level_btn = self._root_node.blit_elements(self._root_node,surface)
        return surface
    
    def check_events(self,event):
        self._root_node.check_events(event, self._root_node)
    
    def get_pontuation(self):
        print(self._root_node.get_pontuation(self._root_node))




class BuildLevels(object):
    
    @classmethod
    def get_levels(cls,surface):
        cls.surface = surface
        cls._levels = []
        cls._files = PropertiesReader()
        cls._levels.append(cls._create_level_1(surface))
        cls._levels.append(cls._create_level_2(surface))
        cls._levels.append(cls._create_level_3(surface))
        cls._levels.append(cls._create_level_4(surface))
        cls._levels.append(cls._create_level_5(surface))
        cls._levels.append(None)
        return cls._levels
    
    
    @classmethod
    def _create_level_1(cls, surface):
        level = Level(surface)
        level._background = pygame.image.load("resources/images/Fase1/Cenários/Parte1/NãoArrumou/Room.png")
        compilador = Compilador(surface, (500,380), [
            "   Ubaldo acaba de acordar e já tem de realizar",
            " a primeira tarefa do dia: arrumar sua cama.", 
            "Ubaldo sabe que é importante manter seu", 
            "ambiente doméstico organizado, além disso sua", 
            "mãe ficaria bastante contente ao ver que seu", 
            "filho está cumprindo com sua obrigação.",])
        level._init_characters.append(compilador)

        node1 = Node(cls.surface,5, (100,20,100,40), (95,30,100,40)).with_value(0.1).with_message(["Manter Ambiente", "    Organizado"]).set_enabled(True)
        node2 = Node(cls.surface,2, (60,65,90,90), (120,130,100,100)).with_value(0.2).with_message([" Arrumar ", " o quarto?"]).set_enabled(True)
        node3 = Node(cls.surface,1, (170,250,100,40), (165,255,100,40)).with_value(0.3).with_message(["Mãe feliz"]).set_enabled(False)
        node4 = Node(cls.surface,1, (30,250,100,40), (25,255,100,40)).with_value(0.1).with_message(["Levar Bronca"]).set_enabled(False)
        node5 = Node(cls.surface,4, (100,340,100,40), (95,345,100,40)).with_value(0.2).with_message(["Fim"]).set_enabled(False)

        level._problem._list_nodes.append(node1)
        level._problem._list_nodes.append(node2)
        level._problem._list_nodes.append(node3)
        level._problem._list_nodes.append(node4)
        level._problem._list_nodes.append(node5)

        node3._left_node = node5
        node4._right_node = node5
        node1._right_node = node2
        node2._left_node = node4
        node2._right_node = node3

        level._problem._root_node = node1
        
        return level

    @classmethod
    def _create_level_2(cls, surface):
        level = Level(surface)
        level._background = pygame.image.load("resources/images/Fase2/Fase2/Cen rios/Parte1/Cozinha.png")
        compilador = Compilador(surface, (500,380), [
            
                            "Chegou a hora do almoço e Ubaldo precisa comer. ",
                            "Sua mãe estabeleceu que a condição para que Ubaldo", 
                            "possa ter sobremesa é comer todo o prato principal.",
                            "Portanto, enquanto houver comida no prato, Ubaldo",
                            "não poderá nem tocar na sobremesa."
                        ])
        level._init_characters.append(compilador)

        node1 = Node(cls.surface,5, (30,20,100,40), (95,30,100,40)).with_value(0.1).with_message(["Manter Ambiente", "    Organizado"]).set_enabled(True)
        node2 = Node(cls.surface,2, (55,70,90,90), (120,130,100,100)).with_value(0.2).with_message([" Arrumar ", " o quarto?"]).set_enabled(True)
        node3 = Node(cls.surface,1, (170,250,100,40), (165,255,100,40)).with_value(0.3).with_message(["Mãe feliz"]).set_enabled(False)
        node4 = Node(cls.surface,1, (30,250,100,40), (25,255,100,40)).with_value(0.1).with_message(["Levar Bronca"]).set_enabled(False)
        node5 = Node(cls.surface,4, (100,340,100,40), (95,345,100,40)).with_value(0.2).with_message(["Fim"]).set_enabled(False)

        level._problem._list_nodes.append(node1)
        level._problem._list_nodes.append(node2)
        level._problem._list_nodes.append(node3)
        level._problem._list_nodes.append(node4)
        level._problem._list_nodes.append(node5)

        node3._left_node = node5
        node4._right_node = node5
        node1._right_node = node2
        node2._left_node = node4
        node2._right_node = node3

        level._problem._root_node = node1
        
        return level


    @classmethod
    def _create_level_3(cls, surface):
        level = Level(surface)
        level._background = pygame.image.load("resources/images/Fase3/Cen rios/Landscape_SemWMpng.png")
        compilador = Compilador(surface, (500,380), [
                            "É hora de se aprontar para ir à escola. O dia, apesar",
                            "de ensolarado, dá indícios de chuva e seria bom que",
                             "Ubaldo estivesse preparado."
                             ])
        
        level._init_characters.append(compilador)

        node1 = Node(cls.surface,5, (100,20,100,40), (90,30,100,40)).with_value(0.1).with_message(["Ir a Escola"]).set_enabled(True)
        node2 = Node(cls.surface,2, (55,65,90,90), (100,140,100,100)).with_value(0.2).with_message(["Levar Guarda","-Chuvas?"]).set_enabled(True)
        node3 = Node(cls.surface,1, (170,250,100,40), (165,255,100,40)).with_value(0.3).with_message(["Ubaldo se", "molha"]).set_enabled(False)
        node4 = Node(cls.surface,1, (30,250,100,40), (25,255,100,40)).with_value(0.1).with_message(["Ubaldo não", "se molha"]).set_enabled(False)
        node5 = Node(cls.surface,4, (100,340,100,40), (95,345,100,40)).with_value(0.2).with_message(["Fim"]).set_enabled(False)

        level._problem._list_nodes.append(node1)
        level._problem._list_nodes.append(node2)
        level._problem._list_nodes.append(node3)
        level._problem._list_nodes.append(node4)
        level._problem._list_nodes.append(node5)

        node3._left_node = node5
        node4._right_node = node5
        node1._right_node = node2
        node2._left_node = node4
        node2._right_node = node3

        level._problem._root_node = node1
        
        return level

    @classmethod
    def _create_level_4(cls, surface):
        level = Level(surface)
        level._background = pygame.image.load("resources/images/Fase4/Cen rios/Parte1/Classroom.png")
        compilador = Compilador(surface, (500,380), [
                        "Ubaldo está na escola no meio da aula de Matemática.", 
                        "O professor decide passar uma simples atividade",
                        "para seus alunos: os alunos devem ler e fazer um",
                        "resumo do que viram em Matrizes até o final da aula."
                    ])
        level._init_characters.append(compilador)

        node1 = Node(cls.surface,5, (100,20,100,40), (90,30,100,40)).with_value(0.1).with_message(["Ir a Escola"]).set_enabled(True)
        node2 = Node(cls.surface,2, (60,65,90,90), (100,140,100,100)).with_value(0.2).with_message(["Levar Guarda","-Chuvas?"]).set_enabled(True)
        node3 = Node(cls.surface,1, (170,250,100,40), (165,255,100,40)).with_value(0.3).with_message(["Ubaldo se", "molha"]).set_enabled(False)
        node4 = Node(cls.surface,1, (30,250,100,40), (25,255,100,40)).with_value(0.1).with_message(["Ubaldo não", "se molha"]).set_enabled(False)
        node5 = Node(cls.surface,4, (100,340,100,40), (95,345,100,40)).with_value(0.2).with_message(["Fim"]).set_enabled(False)

        level._problem._list_nodes.append(node1)
        level._problem._list_nodes.append(node2)
        level._problem._list_nodes.append(node3)
        level._problem._list_nodes.append(node4)
        level._problem._list_nodes.append(node5)

        level._problem._list_nodes.append(node1)
        level._problem._list_nodes.append(node2)
        level._problem._list_nodes.append(node3)
        level._problem._list_nodes.append(node4)
        level._problem._list_nodes.append(node5)

        node3._left_node = node5
        node4._right_node = node5
        node1._right_node = node2
        node2._left_node = node4
        node2._right_node = node3

        level._problem._root_node = node1
        
        return level
    
    @classmethod
    def _create_level_5(cls, surface):
        level = Level(surface)
        level._background = pygame.image.load("resources/images/Fase5/Cen rios/Parte1/Room.png")
        compilador = Compilador(surface, (500,380), ["Mensagem de introdução", "ao level!!"])
        level._init_characters.append(compilador)

        node1 = Node(cls.surface,5, (100,20,100,40), (90,30,100,40)).with_value(0.1).with_message(["Ir a Escola"]).set_enabled(True)
        node2 = Node(cls.surface,2, (60,65,90,90), (100,140,100,100)).with_value(0.2).with_message(["Levar Guarda","-Chuvas?"]).set_enabled(True)
        node3 = Node(cls.surface,1, (170,250,100,40), (165,255,100,40)).with_value(0.3).with_message(["Ubaldo se", "molha"]).set_enabled(False)
        node4 = Node(cls.surface,1, (30,250,100,40), (25,255,100,40)).with_value(0.1).with_message(["Ubaldo não", "se molha"]).set_enabled(False)
        node5 = Node(cls.surface,4, (100,340,100,40), (95,345,100,40)).with_value(0.2).with_message(["Fim"]).set_enabled(False)

        level._problem._list_nodes.append(node1)
        level._problem._list_nodes.append(node2)
        level._problem._list_nodes.append(node3)
        level._problem._list_nodes.append(node4)
        level._problem._list_nodes.append(node5)


        node3._left_node = node5
        node4._right_node = node5
        node1._right_node = node2
        node2._left_node = node4
        node2._right_node = node3

        level._problem._root_node = node1
        
        return level