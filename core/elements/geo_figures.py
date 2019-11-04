import pygame
import sys
sys.path.append("...")

from utils.generators import *

class GeoFigures(object):
    
    def __init__(self):
        pass


    def get_circle(self,surface, r, color, pos):
        return Circle(r,surface, color, pos ).build()

    def get_rectangle(self,surface,color, rect):
        return Rectangle(surface, color, rect ).build()
    
    def get_square(self,surface,color, rect):
        return Square(surface, color, rect ).build()


class Square(object):
    def __init__(self,surface, color, rect):
        self._surface = surface
        self._color = color
        self._rect = rect

    def build(self):
        square = pygame.image.load("resources/images/elements/square.png")
        #square = pygame.transform.rotate(square, 45)
        return self._surface.blit(square, (self._rect[0]+20, self._rect[1]+20))

class Rectangle(object):
    def __init__(self,surface, color, rect):
        self._surface = surface
        self._color = color
        self._rect = rect
        

    def build(self):
        square = pygame.image.load("resources/images/elements/rec.png")
        self._surface.blit(square,(self._rect[0]-20, self._rect[1] -10))
        return self._surface

class Circle(object):

    def __init__(self, r, surface, color, pos):
        self._r = r
        self._surface = surface
        self._color = color 
        self._pos = pos 
        return self.build()
    
    def build(self):
        pygame.draw.circle(self._surface, self._color, self._pos, self._r)
        return self._surface