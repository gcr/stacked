import pygame
import EventList

class TimeController:
    """ Fires off a tick event every frame """
    def __init__(self, event_manager):
        """ This makes a new timer that fires a TickEvent every frame. """
        self.clock = pygame.time.Clock()
        self.ev = event_manager
        
    def tick(self):
        """ Fires every frame """
        self.clock.tick(60)
        self.ev.post(EventList.Tick())
        
class FPSDebugController(TimeController):
    """ Does the same thing as above, only this also displays the FPS
        to the console every second """
    def __init__(self, event_manager):
        TimeController.__init__(self, event_manager)
        self.counter = pygame.time.get_ticks()
        
    def tick(self):
        TimeController.tick(self)
        now = pygame.time.get_ticks()
        if now - self.counter > 1000:
            print(self.clock.get_fps())
            self.counter = pygame.time.get_ticks()
