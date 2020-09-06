#!python3
import json
from motor_events import MotorEvents
from flask import Flask, Response, request, make_response
from flask_cors import CORS

with open('./data-map.json') as data_map_file:

    # Load JSON as dict
    data_map = json.load(data_map_file)
    
    # Create motor object. Pass in GPIO pins that are used for wheels
    motor_events = MotorEvents(data_map['pins'])

# Create flask server application
app = Flask(__name__)
CORS(app)

# Define a route
@app.route(rule='/control', methods=['POST'])
def control():
    print('Control')
    body = request.get_json()
    event_name = body['event']
    event_method = getattr(motor_events, event_name)
    event_response = event_method()
    return make_response({
        'message': event_response if event_response != None else 'Command already in progress...'
    }, 200)

@app.route(rule='/stream', methods=['GET'])
def stream():
    print('Stream')
    return make_response({
        'data': 'stream'
    }, 200)

# Start the server
app.run(host='0.0.0.0')