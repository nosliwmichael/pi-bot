#!/usr/bin/env python
from pynput import keyboard
import sys

class KeyboardListener:

    def __init__(self, keyMap):
        self.keyMap = keyMap
    
    def on_press(self, key):
        try:
            event = self.keyMap.getMotorEvent(key, isPressed=True)
            return self.run_event(key, event)
        except:
            print(sys.exc_info())

    def on_release(self, key):
        try:
            event = self.keyMap.getMotorEvent(key, isPressed=False)
            return self.run_event(key, event)
        except:
            print(sys.exc_info())

    def run_event(self, key, event):
        if event is not None:
            result = event(key)
            if result == 'close':
                return self.close()
        else:
            print('No event for key: {0}'.format(key))

    def start(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
                listener.join()

    def close(self):
        return False
