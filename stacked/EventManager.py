#!/usr/bin/env python
#-*- coding:utf-8 -*-


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
        # Set a default object list if this is a new kind of event
        objects = self.events.setdefault(event.TYPE, [])
        # Send to every object
        for ref in objects:
            if ref() is None:
                # Object doesn't exist anymore, remove it
                objects.remove(ref)
            else:
                ref().notify(event)
