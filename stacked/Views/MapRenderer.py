#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from stacked.Models.Map import Map
import random

class PGView:
    """
        A generic pygame view
    """
    def __init__(self, resolution):
        self.image = pygame.surface.Surface(resolution)
        self.resolution = resolution
    def update(self):
        """
            Updates the screen
        """
        pass
        
class MapRenderer(PGView):
    """
        This renders a map every so often. Whoo!
    """
    def __init__(self, resolution):
        PGView.__init__(self, resolution)
        self.map = Map()
        self.camera = Camera()
        
    def update(self):
        """
            Updates the screen, returns a list of rects that changed.
        """
        self.image.fill([
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        ])
        return [pygame.rect.Rect((0,0), self.resolution)]
        
        
class Camera:
    """
        This handles the camera object stuff.
    """
    def __init__(self):
        self.rect = []
        
    
