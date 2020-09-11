#!python3
# import json
# from motor_events import MotorEvents
import flask
from flask_cors import CORS
import pi_camera

# with open('./data-map.json') as data_map_file:

#     # Load JSON as dict
#     data_map = json.load(data_map_file)
    
#     # Create motor object. Pass in GPIO pins that are used for wheels
#     motor_events = MotorEvents(data_map['pins'])

# Create flask server application
app = flask.Flask(__name__)
CORS(app)

# Define a route
# @app.route(rule='/control', methods=['POST'])
# def control():
#     body = flask.request.get_json()
#     event_name = body['event']
#     event_method = getattr(motor_events, event_name)
#     event_response = event_method()
#     return flask.jsonify(message = event_response if event_response != None else 'Command already in progress..')

@app.route(rule='/pi-cam', methods=['GET'])
def web_stream():
    return flask.render_template('index.html')

@app.route(rule='/video-stream', methods=['GET'])
def stream():
    resp = flask.Response(camera.stream_generator())
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Age"] = 0
    resp.headers["Cache-Control"] = "no-cache, private"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Content-Type"] = "multipart/x-mixed-replace; boundary=FRAME"
    return resp

with pi_camera.StreamPiCamera() as camera:
    # Start the server
    app.run(host='0.0.0.0')
