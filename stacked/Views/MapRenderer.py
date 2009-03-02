#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from stacked.Models.Map import Map
import random
from stacked import EventList

class PGView:
    """
        A generic pygame view
    """
    def __init__(self, event_manager, resolution):
        self.image = pygame.surface.Surface(resolution)
        self.resolution = resolution
        self.ev = event_manager
        
    def update(self):
        """
            Updates the screen
        """
        pass
    
    def notify(self, event):
        pass
        
class MapRenderer(PGView):
    """
        This renders a map every so often. Whoo!
    """
    def __init__(self, ev, resolution):
        PGView.__init__(self, ev, resolution)
        self.map = None
        self.room = None
        self.camera = Camera(resolution)
        self.image.set_colorkey((255,0,255))
        
        for event in [
            EventList.MapLoaded
        ]:
            ev.register_listener(event, self)
        
    def update(self):
        """
            Updates the screen, returns a list of rects that changed.
        """
        if self.map is not None:
            # TODO: Optimize this so only those rects that changed are drawn.
            self.image.fill(self.image.get_colorkey())
            
            return [pygame.rect.Rect((0,0), self.resolution)]
        else:
            # self.map is None
            return [pygame.rect.Rect(0,0,0,0)]
        
        
    def trackmap(self, newmap):
        """
            We'll now render this new map.
        """
        self.map = newmap
        self.room = self.map.rooms[0]
        
        
    def notify(self, event):
        """
            Handle events
        """
        if isinstance(event, EventList.MapLoaded):
            self.trackmap(event.map)
            
        
class Camera:
    """
        This handles the camera object stuff.
    """
    def __init__(self, size):
        self.rect = pygame.rect.Rect((0,0), size)
        
    
