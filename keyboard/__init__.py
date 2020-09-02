#!/usr/bin/env python
import json
from motor_events import MotorEvents
from keyboard_listener import KeyboardListener
from key_map import KeyMap

with open('./data-map.json') as data_map_file:
    
    # Load JSON as dict
    data_map = json.load(data_map_file)
    
    # Create motor object. Pass in GPIO pins that are used for wheels
    motor_events = MotorEvents(data_map['pins'])
    
    # Create key map used to translate key events to motor events
    key_map = KeyMap(data_map['inputs'], motor_events)
    
    # Start keyboard listener to detect key events
    keyboard_listener = KeyboardListener(key_map)
    keyboard_listener.start()