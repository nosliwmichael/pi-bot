#!/usr/bin/env python
import sys

# Check if any command line arguments have been passed
if (len(sys.argv) > 1):
    input_type = sys.argv[1]
    # Load __init__.py from folder depending on input_type
    if (input_type == 'keyboard'):
        import keyboard_input
    elif (input_type == 'http'):
        import http_input