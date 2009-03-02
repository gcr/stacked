#!/usr/bin/env python
#-*- coding:utf-8 -*-

from stacked import EventList
from stacked import ResourceManager
import pygame

class PygameMasterController:

    def __init__(self, eventManager):
        """
            This class handles events from the keyboard
            and posts events of our own to our event manager.
        """
        self.ev = eventManager
        for event in [
            EventList.Tick,
            EventList.NewGame
        ]:
            self.ev.register_listener(event, self)
        
    def notify(self, event):
        if isinstance(event, EventList.Tick):
            # Every tick
            for pyevent in pygame.event.get():
                # What's new in the Pygame worldl?
                if pyevent.type == pygame.QUIT:
                    # User wants to go
                    self.ev.post(EventList.Quit())
        
if __name__ == '__main__':
    print("lolwut?")


