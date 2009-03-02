#!/usr/bin/env python
#-*- coding:utf-8 -*-


import pygame
from stacked import EventList

class DisplayTimeController:
    """
        Fires off a tick event every frame and then a display update
        event afterwards.
    """
    def __init__(self, event_manager, fps):
        """ This makes a new timer that fires a TickEvent every frame. """
        self.clock = pygame.time.Clock()
        self.ev = event_manager
        self.fps = fps
        
    def tick(self):
        """
            Fires a tick event then a display update event
            60 times a second.
        """
        self.clock.tick(self.fps)
        self.ev.post(EventList.Tick())
        self.ev.post(EventList.DisplayUpdate())
        
class FPSDebugController(DisplayTimeController):
    """ 
        Does the same thing as above, only this also displays the FPS
        to the console every second
    """
    def __init__(self, event_manager, fps):
        DisplayTimeController.__init__(self, event_manager, fps)
        self.counter = pygame.time.get_ticks()
        
    def tick(self):
        DisplayTimeController.tick(self)
        now = pygame.time.get_ticks()
        if now - self.counter > 1000:
            print(self.clock.get_fps())
            self.counter = pygame.time.get_ticks()
