#!/usr/bin/env python
#-*- coding:utf-8 -*-


import pygame
from stacked import EventList
import ResourceManager
import sys

class PygameMasterView:
    def __init__(self, event_manager):
        pygame.init()
        # Four steps
        # 1. Set up our variables
        # 2. Set up pygame and draw everything
        # 3. Register with the event manager
        
        # Step 1.
        self.resolution = (800,600)
        self.ev = event_manager
        self.window = pygame.display.set_mode(self.resolution)
        # These "views" are different states the display can be in
        # the game.
        # When we switch views through events, all the layers get cleared
        # and rebuilt. When we get a EventList.DisplayUpdate event,
        # we'll loop
        # through each of the layers and call its update() function,
        # then blit
        # all their surface rects together.
        self.layers = []
        self.views = {'main_menu': [],
            'game': [],
            'options': []}
        
        # Step 2. Draw stuff to the screen
        pygame.display.set_caption("Stacked")
        self.draw_loading_screen()
        
        # Step 3. Event Manager.
        for e in [EventList.DisplayUpdate,
                        EventList.NewGame,
                        EventList.Quit]:
            self.ev.register_listener(e, self)
        
        
    def draw_loading_screen(self):
        """
            Draws a nifty loading page to the screen
        """
        self.window.fill((0,0,0))
        loading_pic = ResourceManager.load_ui_image("loading")
        loading_pic_rect = loading_pic.get_rect()
        loading_pic_rect.center = (self.resolution[0]/2,
                                   self.resolution[1]/2)
        # And draw it to the screen
        self.window.blit(loading_pic, loading_pic_rect)
        pygame.display.update()
        
        
    def notify(self, event):
        """
            Handle events from the event manager
        """
        if isinstance(event, EventList.Quit):
            pygame.quit()
            sys.exit()
        elif isinstance(EventList.NewGame):
            # Change the screen
            self.changescreen('game')
    
