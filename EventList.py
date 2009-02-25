class Event:
    """ A superclass that all of our events will inherit from. """
    TYPE = 0 #note that this MUST be unique!

class Tick(Event):
    """ Fires every frame of the clock """
    TYPE = 1
    
class DisplayUpdate(Event):
    """ Asks the main view to udpate the display """
    TYPE = 2
    
class NewGame(Event):
    """ When a new game is started """
    TYPE = 3
    def __init__(self, map):
        self.map = map
