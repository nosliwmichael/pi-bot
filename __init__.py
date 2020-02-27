from Keyboard import KeyboardListener, KeyMap
from MotorEvents import MotorEvents
import json

with open('./keyMap.json') as keyMap_file:
    data = json.load(keyMap_file)
    motorEvents = MotorEvents()
    keyMap = KeyMap(data, motorEvents)
    keyboard = KeyboardListener(keyMap)
    keyboard.start()
