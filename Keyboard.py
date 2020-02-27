from pynput import keyboard
import sys

class KeyboardListener:

    def __init__(self, keyMap):
        self.keyMap = keyMap
    
    def on_press(self, key):
        try:
            event = self.keyMap.keyPressEvent(key)
            return self.run_event(key, event)
        except:
            print(sys.exc_info())

    def on_release(self, key):
        try:
            event = self.keyMap.keyReleaseEvent(key)
            return self.run_event(key, event)
        except:
            print(sys.exc_info())

    def run_event(self, key, event):
        if event == 'close_event':
            return self.close()
        elif event is not None:
            event(key)
        else:
            print('No event for key: {0}'.format(key))

    def start(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
                listener.join()

    def close(self):
        return False

class KeyMap:

    def __init__(self, keyMap, events):
        self.keyMap = keyMap
        self.events = events

    def keyPressEvent(self, key):
        for k in self.keyMap['keys']:
            keyName = k['name']
            keyEvent = k['pressed']
            event = self.getEvent(key, keyName, keyEvent)
            if (event):
                return event

    def keyReleaseEvent(self, key):
        for k in self.keyMap['keys']:
            keyName = k['name']
            keyEvent = k['released']
            event = self.getEvent(key, keyName, keyEvent)
            if (event):
                return event

    def getEvent(self, key, keyName, keyEvent):
        event = None
        try:
            if ((hasattr(key, 'name') and key.name == keyName and keyEvent) or
                (hasattr(key, 'char') and key.char == keyName and keyEvent)):
                if keyEvent == 'close_event':
                    return keyEvent
                else:
                    event = getattr(self.events, keyEvent)
                    return event
        except:
            print(sys.exc_info())
