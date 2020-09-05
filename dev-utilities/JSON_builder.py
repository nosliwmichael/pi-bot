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
    'left_forward': 23,
    'left_backward': 24,
    'right_forward': 27,
    'right_backward': 22
}
with open('./data-map.json', 'w') as outfile:
    json.dump(data, outfile)
