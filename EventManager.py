import weakref
import EventList

class EventManager:
    """ This class handles most of the communication between the various parts
        of our program. """
    def __init__(self):
        self.events = {}

    def register_listener(self, event, object):
        """ Subscribes the object to every event of eventtype. If eventtype gets
            triggered, the object will be notified through a call to
            object.Notify(event). """
        self.events.setdefault(event.TYPE, []).append(weakref.ref(object))

    def post(self, event):
        """ Posts a new event to every object """
        self.events.setdefault(event.TYPE, [])
        for ref in self.events[event.TYPE]:
            if ref() is None:
                self.events[event.TYPE].remove(ref)
            else:
                ref().notify(event)
