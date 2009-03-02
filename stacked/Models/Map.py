#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame
import rabbyt

class Map:
    """
        This holds a map, full of rooms and dreadful monsters, etc.
    """
    def __init__(self):
        """
            Loads the map with the name name.
        """
        # We don't know how to load a map, so we'll just make our own.
        self.theme = 'arctic'
        self.title = 'Loading Map'
        # just a single room for now
        self.rooms = [Room()]
        
class Room:
    """
        A room from a map. Each map has a list of these.
    """
    def __init__(self):
        """
            Makes a new room
        """
        self.width = 95
        self.height = 96
        # Tiles - tiles[row][colum] - makes the map
        # be stored sideways. WHO CARES? As long as you use
        # this map class, you'll be fine.
        self.bg = []
        self.fg = [] # More tiles
        self.cl = [] # Even more tiles
        self.layers = [self.bg, self.cl, self.fg]
        
        # Fill the layers with empty tiles
        for layer in self.layers:
            self.fillempty(layer)
        
        
        # Make a little border around the collidelayers
        # Top wall
        self.cl[0] = [Tile() for x in self.cl[0]]
        # Bottom wall
        self.cl[-1] = [Tile() for x in self.cl[-1]]
        # Left wall
        for colum in self.cl:
            colum[0] = Tile()
        # Right wall
        for colum in self.cl:
            colum[-1] = Tile()
            
        # HStripes!
        for colum in self.cl:
            colum[::2] = [Tile() for x in colum[::2]]
        # VStripes!
        self.cl[::2] = [[Tile() for y in row] for row in self.cl[::2]]
                
        
        
    def fillempty(self, layer):
        """
            Takes a layer and fills it with emptiness. For debug only.
        """
        for x in xrange(self.width):
            # Create a new column
            layer.append([])
            for y in xrange(self.height):
                layer[x].append(None)
        
        
        
class Tile():
    """
        This contains a tile.
    """
    def __init__(self):
        self.image = rabbyt.Sprite('img/newtile.png')


if __name__ == '__main__':
    print("huh?")


