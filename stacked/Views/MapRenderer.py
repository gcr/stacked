#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
from stacked.Models.Map import Map
from OpenGL.GL import *
import OpenGL.GL
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
        self.layerlist = []
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
            gl = OpenGL.GL
            # Set up the viewport
            gl.glPushMatrix()
            gl.glTranslate(-self.camera.left, -self.camera.top, 0)
            for dlist in self.layerlist:
                gl.glCallList(dlist)
            
            gl.glPopMatrix()     
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
        
        # New display list- Just a tile
        self.tlist = glGenLists(1)
        glNewList(self.tlist, GL_COMPILE)
        glBegin(GL_QUADS)
        glVertex2s(0,0)
        glVertex2s(32,0)
        glVertex2s(32,32)
        glVertex2s(0,32)
        glEnd()
        glEndList()
        
        # New display list - Entire map!
        for layer in self.room.layers:
            # Make a new list and store it in our layers
            newlayer = glGenLists(1)
            self.layerlist.append(newlayer)
            glNewList(newlayer, GL_COMPILE)
            glPushMatrix()
            for row in xrange(len(layer)):
                for colum in xrange(len(layer[row])):
                    if layer[row][colum] is not None:
                        glCallList(self.tlist)
                    glTranslate(32,0,0)
                # New row, move down
                glTranslate(-32*(colum+1),32,0)
            glPopMatrix()
            glEndList()
        print "DLists done"
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
            
