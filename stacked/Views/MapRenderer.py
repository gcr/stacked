#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from stacked.Models.Map import Map
import random
import rabbyt
from stacked import EventList

class PGView:
    """
        A generic pygame view
    """
    def __init__(self, event_manager, resolution):
        self.ev = event_manager
        
    def update(self):
        """
            Updates the screen
        """
        pass
    
    def notify(self, event):
        pass
        
class SpriteTest(PGView):
    def __init__(self, event_manager, resolution):
        self.image = rabbyt.Sprite('img/newtile.png')
        self.image.left = 2
        self.image.top = 0
    def update(self):
        self.image.render()
        
class MapRenderer(PGView):
    """
        This renders a map every so often. Whoo!
    """
    def __init__(self, ev, resolution):
        PGView.__init__(self, ev, resolution)
        self.map = None
        self.room = None
        self.resolution = resolution
        self.camera = Camera(self.ev, resolution)
        for event in [
            EventList.MapLoaded
        ]:
            ev.register_listener(event, self)
        
    def update(self):
        """
            Updates the screen, returns a list of rects that changed.
        """
        if self.map is not None:
            # Set up the viewport
            rabbyt.set_viewport(self.resolution, (self.camera.rect.left, self.camera.rect.top, self.camera.rect.right, self.camera.rect.bottom))
            left = self.camera.rect.left / 32 # Leftmost tile
            top = self.camera.rect.top / 32 # Top tile
            right = self.camera.rect.right / 32 + 1 # Rightmost tile
            bottom = self.camera.rect.bottom / 32 + 1 # Bottommost tile
            
            for layer in self.room.layers:
                for row in layer[top:bottom]:
                    for tile in row[left:right]:
                        if tile is not None:
                            tile.image.render()
                    
            #return [pygame.rect.Rect((0,0), self.resolution)]
            #return dirty_rects
        else:
            # self.map is None
            #return [pygame.rect.Rect(0,0,0,0)]
            pass
        
        
    def trackmap(self, newmap):
        """
            We'll now render this new map.
        """
        self.map = newmap
        self.room = self.map.rooms[0]
        for layer in self.room.layers:
            for row in xrange(len(layer)):
                for colum in xrange(len(layer[row])):
                    if layer[row][colum] is not None:
                        layer[row][colum].image = rabbyt.Sprite('img/newtile.png')
                        layer[row][colum].image.left = colum * 32
                        layer[row][colum].image.bottom = row * 32
        
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
    def __init__(self, event_manager, size):
        self.rect = pygame.rect.Rect((0,0), size)
        self.ev = event_manager
        self.ev.register_listener(EventList.CameraMove, self)
        self.ev.register_listener(EventList.Tick, self)
        
    def notify(self, event):
        if isinstance(event, EventList.Tick):
            self.rect.move_ip(1, 3)
        elif isinstance(event, EventList.CameraMove):
            self.rect.move_ip(event.left, event.top)
        
    
