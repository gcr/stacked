class Event:
    """ A superclass that all of our events will inherit from. """
    TYPE = 0 #note that this MUST be unique!

class Tick(Event):
    """ Fires every frame of the clock """
    TYPE = 1
