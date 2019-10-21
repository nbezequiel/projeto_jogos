


class GeoFigure(object):
    
    def __init__(self):
        pass


    def get_circle(self,surface, r, c):
        pass




class Circle(object):

    def __init__(self, r, c, surface, color, pos):
        self._r = r
        self._c = c
        self._surface = surface
        self._color = color
        self._pos = pos if pos != None  else 0
    
    #def build(self):
        #_circle = pygame.draw.circle(Surface, color, pos, radius, width=0)