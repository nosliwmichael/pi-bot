#!/usr/bin/env python
from Keyboard import KeyboardListener, KeyMap
from MotorEvents import MotorEvents
import json

with open('./keyMap.json') as keyMap_file:
    data = json.load(keyMap_file)
    motorEvents = MotorEvents(left_pins=[11, 13], right_pins=[16, 18])
    keyMap = KeyMap(data, motorEvents)
    keyboard = KeyboardListener(keyMap)
    keyboard.start()
