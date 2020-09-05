#!/usr/bin/env python
import sys

class KeyMap:
    def __init__(self, inputs, motor_events):
        self.inputs = inputs
        self.motor_events = motor_events

    def getMotorEvent(self, key, is_pressed):
        for i in self.inputs:
            inputName = i['name']
            inputEvent = i['pressed' if is_pressed else 'released']
            try:
                if (inputEvent and
                    (hasattr(key, 'name') and key.name == inputName) or
                    (hasattr(key, 'char') and key.char == inputName)):
                    return getattr(self.motor_events, inputEvent)
            except:
                print(sys.exc_info())
