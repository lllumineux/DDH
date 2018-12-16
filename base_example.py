import json

documentation = {
    'func_name': {
        'description': '',
        'syntax': '',
        'args': {
            'arg': {
                'description': '',
                'type': '',
                'default_value': '',
                'addition': ''
            }
        },
        'return_value': ''
    }
}

with open('documentation', 'w+', encoding='utf-8') as file:
    json.dump(documentation, file)
