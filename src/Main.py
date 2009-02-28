#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
from EventManager import EventManager
from Views.PygameMasterView import PygameMasterView
from Views.PygameMasterController import PygameMasterController

import Controllers.TimeKeepers
from Models.Game import Game

def main():
    ev = EventManager() # Keep track of it all
    timer = TimeKeepers.DisplayTimeController(ev) # Time it all
    game = Game(ev) # Control it all
    pycont = PygameMasterController(ev) # Get it all
    pyview = PygameMasterView(ev) # Draw it all
    
    while 1:
        timer.tick()
    
if __name__ == "__main__":
    main()
    
