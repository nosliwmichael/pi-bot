import json

## BUILD JSON FILE ##
data = {}
data['keys'] = [
    {
        "name": "up",
        "pressed": "up_event",
        "released": "stop_event"
    },
    {
        "name": "down",
        "pressed": "down_event",
        "released": "stop_event"
    },
    {
        "name": "left",
        "pressed": "left_event",
        "released": "stop_event"
    },
    {
        "name": "right",
        "pressed": "right_event",
        "released": "stop_event"
    },
    {
        "name": "esc",
        "pressed": "close_event",
        "released": "close_event"
    }
]
with open('../keyMap.json', 'w') as outfile:
    json.dump(data, outfile)
