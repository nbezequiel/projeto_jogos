
import pygame
from pygame.locals import *
from core.gameSection import Menu, GameSection



class LoopGameEvents(object):
    
    
    def __init__(self, screen):
        self._game = None
        self._screen = screen
        self._current_display = None
        self._surfaces_to_update = []
        self._menu = Menu(screen)

    def catch_events(self,event, myfont):
        if self._current_display == None:
            self._current_display = self._menu
            self._surfaces_to_update.append(self._current_display.blit_elements(event, myfont))
        
        choice = self._current_display.check_events(event)    
        
        if choice == 1:
            self._current_display = GameSection(self._screen)
            self._surfaces_to_update.append(self._current_display.blit_elements())
        
        if choice == 2:
            pass
        
        if choice == 3:
            pass

        return self._surfaces_to_update

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('Game Name')
    pygame.font.init() 
    myfont = pygame.font.SysFont('freesans', 40)

  
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    
    screen.blit(background, (0, 0))
    pygame.display.flip()

    loop_events = LoopGameEvents(screen)

    # Event loop
    while 1:
        

        for event in pygame.event.get():
            if event.type == QUIT:
                return
                
            for surface in loop_events.catch_events(event, myfont):
                background.blit(surface,(0,0))
       
       

        
        screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(100)

main()



