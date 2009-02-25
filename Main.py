import time
from EventManager import EventManager
from PygameMasterView import PygameMasterView
import TimeKeepers
from Game import Game

def main():
    ev = EventManager() # Keep track of it all
    timer = TimeKeepers.FPSDebugController(ev) # Time it all
    game = Game(ev) # Control it all
    pyview = PygameMasterView(ev) # Draw it all
    
    while 1:
        timer.tick()
    
if __name__ == "__main__":
    main()
    
