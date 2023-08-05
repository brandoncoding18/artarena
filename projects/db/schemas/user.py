from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from collections import OrderedDict

db = MongoClient("mongodb://localhost:27019/")['mydatabase']

user_schema = {
    'id': {
        'type': 'int', 
        'minlength': 1,
        'required': True,
    },
    'username': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    }

    
}

collection = 'Userinformation'
validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
required = []

for field_key in user_schema:
    field = user_schema[field_key]
    properties = {'bsonType': field['type']}
    minimum = field.get('minlength')

    if type(minimum) == int:
        properties['minimum'] = minimum

    if field.get('required') is True: required.append(field_key)

    validator['$jsonSchema']['properties'][field_key] = properties

if len(required) > 0:
    validator['$jsonSchema']['required'] = required

query = [('collMod', collection),
         ('validator', validator)]

try:
    db.create_collection(collection)
except CollectionInvalid:
    pass

command_result = db.command(OrderedDict(query))