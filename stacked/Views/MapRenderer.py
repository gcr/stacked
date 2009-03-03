#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from stacked.Models.Map import Map
from OpenGL.GL import *
import random
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
        
class MapRenderer(PGView):
    """
        This renders a map every so often. Whoo!
    """
    def __init__(self, ev, resolution):
        PGView.__init__(self, ev, resolution)
        self.map = None
        self.room = None
        self.resolution = resolution
        self.camera = pygame.rect.Rect((0,0), self.resolution)
        self.dlist = 0
        for event in [
            EventList.MapLoaded,
            EventList.Tick
        ]:
            ev.register_listener(event, self)
        
    def update(self):
        """
            Updates the screen, returns a list of rects that changed.
        """
        if self.map is not None:
            # Set up the viewport
            glPushMatrix()
            glLoadIdentity()
            glTranslate(-self.camera.left, -self.camera.top, 0)
            glCallList(self.dlist)
               
            glPopMatrix()     
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
        
        # New display list
        self.dlist = glGenLists(1)
        glNewList(self.dlist, GL_COMPILE)
        glPushMatrix()
        for layer in [self.room.cl]:
            for row in xrange(len(layer)):
                for colum in xrange(len(layer[row])):
                    if layer[row][colum] is not None:
                        glBegin(GL_QUADS)
                        glVertex(0,0)
                        glVertex(32,0)
                        glVertex(32,32)
                        glVertex(0,32)
                        glEnd()
                    glTranslate(32,0,0)
                # New row, move down
                glTranslate(-32*(colum+1),32,0)
        glPopMatrix()
        glEndList()
        print "DList done"
#        for layer in self.room.layers:
#            for row in xrange(len(layer)):
#                for colum in xrange(len(layer[row])):
#                    if layer[row][colum] is not None:
#                        layer[row][colum].image = rabbyt.Sprite('img/newtile.png')
#                        layer[row][colum].image.left = colum * 32
#                        layer[row][colum].image.bottom = row * 32
        
    def notify(self, event):
        """
            Handle events
        """
        if isinstance(event, EventList.MapLoaded):
            self.trackmap(event.map)
        elif isinstance(event, EventList.Tick):
            self.camera.move_ip(2,2)
            
