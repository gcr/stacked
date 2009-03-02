#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pygame

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
        self.rooms = []
        
class Room:
    """
        A room from a map. Each map has a list of these.
    """
    def __init__(self):
        """
            Makes a new room
        """
        self.width = 3
        self.height = 5
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
        # Left wall
        self.cl[0] = [Tile() for x in self.cl[0]]
        # Right wall
        self.cl[-1] = [Tile() for x in self.cl[-1]]
        # Top wall
        for colum in self.cl:
            colum[0] = Tile()
        # Bottom wall
        for colum in self.cl:
            colum[-1] = Tile()
        
        
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
        self.texture = pygame.Surface((32, 32))
        self.texture.fill((255,0,0))


if __name__ == '__main__':
    print("huh?")


