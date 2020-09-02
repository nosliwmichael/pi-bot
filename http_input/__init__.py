#!/usr/bin/env python
import json
from motor_events import MotorEvents

with open('./data-map.json') as data_map_file:
    
    # Load JSON as dict
    data_map = json.load(data_map_file)
    
    # Create motor object. Pass in GPIO pins that are used for wheels
    motor_events = MotorEvents(data_map['pins'])