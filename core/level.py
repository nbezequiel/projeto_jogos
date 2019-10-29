import pygame
import sys
sys.path.append("..")
from core.elements.geo_figures import *
from .elements.character import Compilador

pygame.display.set_caption('Game Name')
pygame.font.init() 
myfont = pygame.font.SysFont('loma', 12)

#from ..utils.properties_reader import PropertiesReader
from utils.properties_reader import PropertiesReader

from pygame.locals import *

class Level(object):

    def __init__(self, surface, own_events):
        self._surface = surface
        self._score = 0 
        self._own_events = own_events
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
        self._surface.blit(self._background, (0,0))
        for character in self._init_characters:
            character.blit_elements(self._surface)



        if self._init_screen == True: return

        
        
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
        self._own_events(event)

    def timer_start(self):
        pass

    def start_final_animation(self):
        pass
    

class Node(object):

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


    def set_text_ballon_format(self):
        
        if self._node_type == 1 or self._node_type == 4 :
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

    def blit_elements(self, node, surface):
        if node == None: return
        
        if node._node_type == 4 and node._enabled == True : 
            pygame.draw.rect(surface,(255, 255, 255),(800,560, 100,40), 0)

        if node._enabled == True and node._node_type != 0: 
            node._text_ballon = node.set_text_ballon_format()
            y_text = 0
            for text in node._message:
                pos = node._text_pos
                surface.blit(myfont.render(text, False,(0,0,0)),(pos[0],pos[1] +y_text, pos[2], pos[3]))
                y_text += 13
            #surface.blit(self._arrow, rect)
        
        if node._right_node != None:
            if node._enabled == True and node._right_node._node_type == 4 or node._right_node._node_type == 2:
                node._right_node._enabled = True
                self.blit_elements(node._right_node, surface)
                return
        
        if node._left_node != None :

            if node._enabled == True and node._left_node._node_type == 4 or node._left_node._node_type == 2:
                node._left_node._enabled = True
                self.blit_elements(node._left_node, surface)
                return

        if node._right_node != None and node._left_node != None:
            self.blit_elements(node._right_node, surface)
            self.blit_elements(node._left_node, surface)
        
        if node._node_type == 2 and node._left_node._enabled == False and node._right_node._enabled == False:
            pygame.draw.rect(surface,(0, 0, 0),(400,240, 100,40), 0)
            surface.blit(myfont.render("Sim", False, (255,255,255)),(430,250, 100,40))
            pygame.draw.rect(surface,(0, 0, 0),(400,300, 100,40), 0)
            surface.blit(myfont.render("Não", False, (255,255,255)),(430,310, 100,40))
        return surface

    

class Problem(object):

    def __init__(self):
        self._root_node = None
        self._animation = None
        self._list_nodes = []


    def get_score(self):
        return reduce(lambda n : n._value if n._enabled == True else 0,self._list_nodes)


    def start_animation(self):
        pass

    def blit_elements(self, surface):
        self._root_node.blit_elements(self._root_node,surface)
        return surface




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
        return cls._levels
    
    
    @classmethod
    def _create_level_1(cls, surface):
        def a(event):pass # mock event
        level = Level(surface, a)
        level._background = pygame.image.load("resources/images/backgrounds/back_fase1.png")
        compilador = Compilador(surface, (100,100), ["Mensagem de introdução", "ao level!!"])
        level._init_characters.append(compilador)

        node1 = Node(cls.surface,1, (80,20,100,40), (90,30,100,40)).with_value(0.1).with_message(["Hora do almoço"]).set_enabled(True)
        node2 = Node(cls.surface,2, (60,90,100,100), (90,150,100,100)).with_value(0.1).with_message(["Hora do", "almoço"]).set_enabled(True)
        node3 = Node(cls.surface,1, (150,230,100,40), (160,240,100,40)).with_value(0.1).with_message(["Hora do almoço"]).set_enabled(False)
        node4 = Node(cls.surface,1, (10,230,100,40), (20,240,100,40)).with_value(0.1).with_message(["Hora do almoço"]).set_enabled(False)
        node5 = Node(cls.surface,4, (80,300,100,40), (90,300,100,40)).with_value(0.1).with_message(["Hora do almoço"]).set_enabled(False)

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
        pass

    @classmethod
    def _create_level_3(cls, surface):
        pass

    @classmethod
    def _create_level_4(cls, surface):
        pass