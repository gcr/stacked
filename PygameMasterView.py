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
        # Load a pretty picture
        self.window.fill((255,255,255))
        loading_pic = pygame.image.load("img/UI/loading.png")
        loading_pic_rect = loading_pic.get_rect()
        loading_pic_rect.center = (self.resolution[0]/2,
                                   self.resolution[1]/2)
        # And draw it to the screen
        self.window.blit(loading_pic, loading_pic_rect)
        pygame.display.update()
        
        # Step 2.
        self.ev = eventManager
        self.ev.register_listener(EventList.DisplayUpdate, self)
        self.ev.register_listener(EventList.NewGame, self)
        
        # Step 3.
        # These "views" are different states the display can be in the game.
        # When we switch views through events, all the layers get cleared
        # and rebuilt. When we get a EventList.DisplayUpdate event, we'll loop
        # through each of the layers and call its update() function, then blit
        # all their surface rects together.
        self.layers = []
        self.views = {'main_menu': [],
            'game': [],
            'options': []}
        
    def notify(self, event):
        pass
