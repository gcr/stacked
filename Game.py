import pygame
import EventList

class Game:
    """ This class holds the logic to make a new game. """
    def __init__(self, event_manager):
        self.ev = event_manager
        self.map = []
        self.players = []
        
        # Listen for new game events
        self.ev.register_listener(EventList.NewGame, self)
