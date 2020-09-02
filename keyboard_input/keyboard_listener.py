#!/usr/bin/env python
import sys
from pynput import keyboard

class KeyboardListener:

    def __init__(self, key_map):
        self.key_map = key_map
    
    def on_press(self, key):
        try:
            event = self.key_map.getMotorEvent(key, is_pressed=True)
            return self.run_event(key, event)
        except:
            print(sys.exc_info())

    def on_release(self, key):
        try:
            event = self.key_map.getMotorEvent(key, is_pressed=False)
            return self.run_event(key, event)
        except:
            print(sys.exc_info())

    def run_event(self, key, event):
        if event is not None:
            result = event()
            if result == 'close':
                return self.close()

    def start(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
                listener.join()

    def close(self):
        return False
