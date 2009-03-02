#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Event:
    """ A superclass that all of our events will inherit from. """
    TYPE = 0 #note that this MUST be unique!

class Tick(Event):
    """ 
        Fires every frame of the clock. Usually, a TimeController
        or sommat like that will fire this.
    """
    TYPE = 1
    
class DisplayUpdate(Event):
    """ Asks the main view to udpate the display """
    TYPE = 2
    
class ChangeScreenRequest(Event):
    """ 
        When the user wants to switch which 'mode' we're
        in, PygameMasterView and friends will switch the sprite
        groups they choose to draw.
    """
    TYPE = 3
    def __init__(self, screen):
        self.screen = screen
        
class NewGame(Event):
    """
        When a new game is started, Game and the like will
        jump into action and load a new map.
    """
    TYPE = 4
        
class Quit (Event):
    """ When the user gets bored and wants to leave """
    TYPE = 5
    
class MapLoaded(Event):
    """ When the user loads a new map """
    TYPE = 6
    def  __init__(self, map):
        self.map = map



if __name__ == '__main__':
    print("that was unexpected")
    
