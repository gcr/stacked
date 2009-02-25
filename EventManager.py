import time
import weakref
import EventList

class ListenerTest:
    def __init__(self):
        self.count = 0
    def notify(self, event):
        self.count += 1

class EventManager:
    """ This class handles most of the communication between the various parts
        of our program. """
    def __init__(self):
        self.events = {}

    def RegisterListener(self, event, object):
        """ Subscribes the object to every event of eventtype. If eventtype gets
            triggered, the object will be notified through a call to
            object.Notify(event). """
        self.events.setdefault(event.TYPE, []).append(weakref.ref(object))

    def Post(self, event):
        """ Posts a new event to every object """
        for ref in self.events[event.TYPE]:
            if ref() is None:
                self.events[event.TYPE].remove(ref)
            else:
                ref().notify(event)

def main():
	test = ListenerTest()
	test2 = ListenerTest()
	ev = EventManager()
	ev.RegisterListener(EventList.Event, test)
	ev.RegisterListener(EventList.Event, test2)
	
	for x in xrange(500000):
	    ev.Post(EventList.Event())
	
	del test2
	
	for x in xrange(500000):
	    ev.Post(EventList.Event())
	print(test.count)
	

import cProfile
cProfile.run('main()')
