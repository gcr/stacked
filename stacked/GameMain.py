#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
from stacked.EventManager import EventManager
from stacked.Views.PygameMasterView import PygameMasterView
from stacked.Controllers.PygameMasterController import PygameMasterController

from stacked.Controllers import TimeKeepers
from stacked.Models.Game import Game

def run():
    ev = EventManager() # Keep track of it all
    timer = TimeKeepers.DisplayTimeController(ev) # Time it all
    game = Game(ev) # Control it all
    pycont = PygameMasterController(ev) # Get it all
    pyview = PygameMasterView(ev) # Draw it all
    
    while 1:
        timer.tick()
    
if __name__ == "__main__":
    print("You should go to the previous directory and run python Kickstart.py")
    