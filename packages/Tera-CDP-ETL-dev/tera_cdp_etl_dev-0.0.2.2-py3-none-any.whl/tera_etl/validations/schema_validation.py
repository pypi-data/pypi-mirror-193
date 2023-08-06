from datetime import datetime
from dateutil.parser import parse
import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')


def build_path(path, key):
    return key if len(path) == 0 else path + '.' + key


def validate_array(m, data, path):
    result = []
    for i in range(len(data)):
        result += validate(m, data[i], path + '[{}]'.format(i))
    return result


def validate_type(value, type_str):
    if type_str == 'string':
        return type(value) is str
    elif type_str == 'bool':
        return type(value) is bool
    elif type_str == 'int':
        return type(value) is int
    elif type_str == 'float':
        return type(value) is float
    elif type_str == 'datetime':
        try: 
            parse(value, fuzzy=False)
            return True
        except ValueError:
            return False
    elif type_str == 'null':
        return value is None
    elif type_str == 'number':
        return type(value) in [int, float]
    elif type_str == 'object':
        # Do not validate the object's structure
        return type(value) is dict
    elif type_str == 'any':
        return True
    else:
        raise Exception('Model type is not valid')


def get_default_value(m_key):
    # Model field is an array of objects
    # case1:     foo: [{bar: ['string', 'value']}]
    if type(m_key) is list and type(m_key[0]) is dict:
        return []

    # Model field is an object
    # case2:     foo: {bar: ['string', 'value']}
    if type(m_key) is dict:
        res = {}
        for key in m_key.keys():
            res[key] = get_default_value(m_key[key])
        return res

    # case3:     foo: ['string', 'value']
    return m_key[1]


def validate(schema, data, path=''):
    result = []

    # Verify that passed document is a dictionary
    if type(data) is not dict:
        raise Exception('Data passed to "validate" function must be a dictionary')

    # Check for extra fields in mongo doc
    for field in data:
        if field not in schema.keys():
            fullpath = build_path(path, field)
            field_type = type(data[field]).__name__
            error_response = {
                'msg': '[+] Extra field: "{}" having type: "{}"'.format(fullpath, field_type),
                'type': 'extra_field',
                'path': fullpath,
                'field_type': field_type
            }
            result.append(error_response)

    for key in schema:
        if key not in data:
            fullpath = build_path(path, key)
            error_response = {
                'msg': '[-] Missing field: "{}"'.format(fullpath),
                'type': 'missing_field',
                'path': fullpath,
                'default_value': get_default_value(schema[key])
            }
            result.append(error_response)
            continue

        # Model field is an array of objects
        if type(schema[key]) is list and type(schema[key][0]) is dict:
            result += validate_array(schema[key][0], data[key], build_path(path, key))
            continue

        # Model field is an object
        if type(schema[key]) is dict:
            result += validate(schema[key], data[key], build_path(path, key))
            continue

        # Model field is an array of strings (means data value can have any of the presented types)
        # ex: [['number', 'string'], 1]
        if type(schema[key]) is list and type(schema[key][0]) is list and type(schema[key][0][0]) is str:
            res = any(validate_type(data[key], cur_type) for cur_type in schema[key][0])
            if not res:
                fullpath = build_path(path, key)
                expected = schema[key][0]
                found = type(data[key]).__name__
                error_response = {
                    'msg': '[*] "{}" has wrong type. Expected one of: "{}", found: "{}"'.format(fullpath,expected,found),
                    'type': 'wrong_type',
                    'path': fullpath,
                    'expected': expected,
                    'found': found,
                }
                result.append(error_response)
            continue
        
        
        # ex: ["string", "null"]
        if type(schema[key]) is list and type(schema[key][0]) is str:
            res = any(validate_type(data[key], cur_type) for cur_type in schema[key])
            if not res:
                fullpath = build_path(path, key)
                expected = schema[key]
                found = type(data[key]).__name__
                error_response = {
                    'msg': '[*] "{}" has wrong type. Expected one of: "{}", found: "{}"'.format(fullpath,expected,found),
                    'type': 'wrong_type',
                    'path': fullpath,
                    'expected': expected,
                    'found': found,
                }
                result.append(error_response)
            continue

        # Model field is an array and 1st element is a string
        res = None
        try:
            res = validate_type(data[key], schema[key])
        except Exception as e:
            raise Exception('[@@@] Model is not valid: "{}" has incorrect type: "{}"'.format(key, schema[key]))
        if not res:
            fullpath = build_path(path, key)
            expected = schema[key][0]
            found = type(data[key]).__name__
            error_response = {
                'msg': '[*] "{}" has wrong type. Expected: "{}", found: "{}"'.format(fullpath, expected, found),
                'type': 'wrong_type',
                'path': fullpath,
                'expected': expected,
                'found': found,
            }
            result.append(error_response)
    return result
