#!/usr/bin/env python
from Keyboard import KeyboardListener, KeyMap
from MotorEvents import MotorEvents
import json

with open('./keyMap.json') as keyMap_file:
    data = json.load(keyMap_file)
    motorEvents = MotorEvents(left_pins=[5, 6], right_pins=[13, 19])
    keyMap = KeyMap(data, motorEvents)
    keyboard = KeyboardListener(keyMap)
    keyboard.start()
