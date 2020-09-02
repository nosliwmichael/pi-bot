import json

## BUILD JSON FILE ##
data = {}
data['inputs'] = [
    {
        'name': 'up',
        'pressed': 'up_event',
        'released': 'stop_event'
    },
    {
        'name': 'down',
        'pressed': 'down_event',
        'released': 'stop_event'
    },
    {
        'name': 'left',
        'pressed': 'left_event',
        'released': 'stop_event'
    },
    {
        'name': 'right',
        'pressed': 'right_event',
        'released': 'stop_event'
    },
    {
        'name': 'space',
        'pressed': 'stop_event',
        'released': None
    },
    {
        'name': 'esc',
        'pressed': 'close_event',
        'released': None
    }
]
data['pins'] = {
    'back_left': 11,
    'back_right': 16,
    'front_left': 13,
    'front_right': 18
}
with open('./data-map.json', 'w') as outfile:
    json.dump(data, outfile)
