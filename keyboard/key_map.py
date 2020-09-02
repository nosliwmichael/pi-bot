#!/usr/bin/env python
import sys

class KeyMap:
    def __init__(self, inputs, motor_events):
        self.inputs = inputs
        self.motor_events = motor_events

    def getMotorEvent(self, key, isPressed):
        for i in self.inputs:
            inputName = i['name']
            inputEvent = i['pressed' if isPressed else 'released']
            event = None
            try:
                if (inputEvent and
                    (hasattr(key, 'name') and key.name == inputName) or
                    (hasattr(key, 'char') and key.char == inputName)):
                    event = getattr(self.motor_events, inputEvent)
                    return event
            except:
                print(sys.exc_info())