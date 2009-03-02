#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame
from stacked import EventList
from stacked.Views.MapRenderer import MapRenderer
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
        self.current_views = []
        self.view_classes = {
            'main_menu': [],
            'game': [MapRenderer],
            'options': []
        }
        
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
        
        
    def update_display(self):
        """
            Updates the screen every frame
        """
        changed_rects = []
        for view in self.current_views:
            changed_rects.extend( view.update() )
            self.window.blit(view.image, (0,0))
            
        pygame.display.update(changed_rects)
        
    def change_screen(self, new_screen):
        """
            This changes what subviews we draw to the screen.
            e.g. self.changescreen('game') will give us a map renderer,
            a HUD, etc.
        """
        # Empty out the old
        for view in self.current_views:
            del view
        self.current_views = []
        
        # In with the new
        for new_view in self.view_classes[new_screen]:
            self.current_views.append(new_view(self.ev, self.resolution))
    
    
    def notify(self, event):
        """
            Handle events from the event manager
        """
        if isinstance(event, EventList.Quit):
            pygame.quit()
            sys.exit()
        elif isinstance(event, EventList.NewGame):
            # Change the screen
            self.change_screen('game')
        elif isinstance(event, EventList.DisplayUpdate):
            # Update the display
            self.update_display()
    
