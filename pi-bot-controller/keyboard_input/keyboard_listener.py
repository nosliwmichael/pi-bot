#!python3
import sys
from pynput import keyboard

class KeyboardListener:

    def __init__(self, key_map):
        self.key_map = key_map

    def start(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
                listener.join()
    
    def on_press(self, key):
        return self.run_event(key=key, is_pressed=True)

    def on_release(self, key):
        return self.run_event(key=key, is_pressed=False)

    def run_event(self, key, is_pressed):
        try:
            event = self.key_map.getMotorEvent(key=key, is_pressed=is_pressed)
            if event is not None:
                result = event()
                if result != None:
                    print(result)
                    if result == 'close':
                        return False
        except:
            print(sys.exc_info())