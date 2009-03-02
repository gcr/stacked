#!/usr/bin/env python
#-*- coding:utf-8 -*-


import pygame
from stacked import EventList

class Game:
    """ This class holds the logic to make a new game. """
    def __init__(self, event_manager):
        self.ev = event_manager
        self.map = None
        self.players = []
        
        # Listen for new game events
        for event in [
            EventList.NewGame
        ]:
            self.ev.register_listener(event, self)
        
        self.ev.register_listener(EventList.NewGame, self)
        
    def notify(self, event):
        pass
