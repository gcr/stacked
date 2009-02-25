import pygame
import EventList

class PygameMasterView:
    def __init__(self, eventManager):
        pygame.init()
        # Three steps
        # 1. Set up pygame
        # 2. Set up the event manager and listen for events
        # 3. Set up the views
        
        # Step 1.
        self.resolution = (800,600)
        self.window = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Stacked")
        self.window.fill((255,255,255))
        # Load a pretty picture
        loading_pic = pygame.image.load("img/UI/loading.png")
        loading_pic_rect = loading_pic.get_rect()
        loading_pic_rect.center = (self.resolution[0]/2,
                                   self.resolution[1]/2)
        # And draw it to the screen
        self.window.blit(loading_pic, loading_pic_rect)
        pygame.display.update()
        
        # Step 2.
        self.ev = eventManager
        self.ev.register_listener(EventList.Tick, self)
        
        
    def notify(self, event):
        pygame.display.flip()
        
