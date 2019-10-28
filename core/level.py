import pygame
import sys
sys.path.append("..")
from core.elements.geo_figures import *
pygame.display.set_caption('Game Name')
pygame.font.init() 
myfont = pygame.font.SysFont('freesans', 12)

#from ..utils.properties_reader import PropertiesReader
from utils.properties_reader import PropertiesReader

from pygame.locals import *

class Level(object):

    def __init__(self, surface, own_events):
        self._surface = surface
        self._score = 0 
        self._own_events = own_events
        self._characters = []
        self.clickable_choices = []
        self._background = None
        self._timer = None ## time progressivo
        self._problem =  Problem()
        self._end_animation =  self.check_animation(self._problem)
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
        
        self._surface = self._problem.blit_elements(self._surface)
       
        for character in self._characters:
            self._surface.blit(character._image)
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

    def __init__(self, surface, node_type, pos):
        self._node_type = node_type
        self._pos = pos 
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
        
        if self._node_type == 1:
            x = GeoFigures()
            return x.get_rectangle(self._surface,(255,255,255), self._pos)



    def show(self):
        self._enabled = True 
        pass
    
    def hide(self):
        self._enabled = False
        pass ###esconde tudo dele e filhos

    def blit_elements(self, node, surface):
        if node == None: return
        if node._enabled == True and node._node_type != 0: 
            self._text_ballon = self.set_text_ballon_format()
            surface.blit(myfont.render(self._message, False,(0,0,0)),(self._pos[0]+10,self._pos[1]+10,self._pos[2],self._pos[3]))
            #surface.blit(self._arrow, rect)
        if node._left_node == None and node._right_node != None:
            surface = self.blit_elements(node._right_node, surface)
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
        def a(event):pass
        level = Level(surface, a)
        level._background = pygame.image.load("resources/images/backgrounds/exemple.jpeg")
        node1 = Node(cls.surface,1, (70,70,100,30)).with_value(0.1).with_message("Hora do almoço").set_enabled(True)
        node2 = Node(cls.surface,1, (70,100,100,100)).with_value(0.1).with_message("""
        Hora do almoço
        """).set_enabled(True)
        level._problem._list_nodes.append(node1)
        level._problem._list_nodes.append(node2)
        node1._right_node = node2
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