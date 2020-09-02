#!/usr/bin/env python
import sys

if (len(sys.argv) > 1):
    input_type = sys.argv[1]
    if (input_type == 'keyboard'):
        from keyboard.keyboard_listener import KeyboardListener
        from keyboard.key_map import KeyMap
    elif (input_type == 'http'):
        print input_type