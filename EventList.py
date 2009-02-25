class Event:
    """ A superclass that all of our events will inherit from. """
    TYPE = 0 #note that this MUST be unique!

class Tick(Event):
    """ Fires every frame of the clock """
    TYPE = 1

class NewGame(Event):
    """ When a new game is started """
    TYPE = 2
    def __init__(self, map):
        self.map = map
