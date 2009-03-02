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
    
class SolidBlack(PGView):
    def __init__(self, event_manager, resolution):
        print "I got called anyway"
        PGView.__init__(self, event_manager, resolution)
        self.image.fill((0,0,0))
        
class MapRenderer(PGView):
    """
        This renders a map every so often. Whoo!
    """
    def __init__(self, ev, resolution):
        PGView.__init__(self, ev, resolution)
        self.map = None
        self.room = None
        self.camera = Camera(self.ev, resolution)
        self.colorkey = (255,0,255)
        self.image.set_colorkey(self.colorkey)
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
            self.image.fill(self.colorkey)
            dirty_rects = []
            left = self.camera.rect.left / 32 # Leftmost tile
            top = self.camera.rect.top / 32 # Top tile
            right = self.camera.rect.right / 32 + 1 # Rightmost tile
            bottom = self.camera.rect.bottom / 32 + 1 # Bottommost tile
            mod_left = self.camera.rect.left % 32 # Offset
            mod_top = self.camera.rect.top % 32 # Offset
            
            for layer in self.room.layers:
                cur_x = 0 - mod_left
                cur_y = 0 - mod_top
                for colum in layer[left:right]:
                    cur_y = 0 - mod_top
                    for tile in colum[top:bottom]:
                        if tile is not None:
                            self.image.blit(tile.image,
                                (cur_x, cur_y))
                            dirty_rects.append(pygame.rect.Rect(
                                (cur_x, cur_y), (32, 32)))
                        cur_y += 32
                    cur_x += 32
                    
            return [pygame.rect.Rect((0,0), self.resolution)]
            #return dirty_rects
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
    def __init__(self, event_manager, size):
        self.rect = pygame.rect.Rect((0,0), size)
        self.ev = event_manager
        self.ev.register_listener(EventList.CameraMove, self)
        self.ev.register_listener(EventList.Tick, self)
        
    def notify(self, event):
        if isinstance(event, EventList.Tick):
            self.rect.move_ip(0, 3)
        elif isinstance(event, EventList.CameraMove):
            self.rect.move_ip(event.left, event.top)
        
    
