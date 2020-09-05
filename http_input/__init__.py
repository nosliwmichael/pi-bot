#!python3
import json
from motor_events import MotorEvents
from flask import Flask, request

with open('./data-map.json') as data_map_file:

    # Load JSON as dict
    data_map = json.load(data_map_file)
    
    # Create motor object. Pass in GPIO pins that are used for wheels
    motor_events = MotorEvents(data_map['pins'])

# Create flask server application
app = Flask(__name__)

# Define a route
@app.route(rule='/pi-bot', methods=['POST'])
def hello_world():
    body = request.get_json()
    event_name = body['event']
    event = getattr(motor_events, event_name)
    response = event()
    return response if response != None else 'Command already in progress...'

# Start the server
app.run()