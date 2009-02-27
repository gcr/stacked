class Event:
    """ A superclass that all of our events will inherit from. """
    TYPE = 0 #note that this MUST be unique!

class Tick(Event):
    """ Fires every frame of the clock """
    TYPE = 1
    
class DisplayUpdate(Event):
    """ Asks the main view to udpate the display """
    TYPE = 2
    
class ChangeScreenRequest(Event):
    """ When the user wants to switch which 'mode' we're in """
    TYPE = 3
    def __init__(self, screen):
        self.screen = screen
        
class NewGame(Event):
    """ When a new game is started """
    TYPE = 4
    def __init__(self, map):
        self.map = map
        
class Quit (Event):
    """ When the user gets bored and wants to leave """
    TYPE = 5



if __name__ == '__main__':
    print("that was unexpected")
    
