MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'recipes'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
RECIPE_SCHEMA = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'required': True
    },
    'description': {
        'type': 'string',
        'minlength': 1,
        'required': True
    },
    'steps': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'instruction_text': {'type': 'string'},
                'notes': {'type': 'string'}
            }
        }
    },
    'ing': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'amount': {'type': 'string'},
                'name': {'type': 'string'}
            }
        }
    }
}

X_DOMAINS = ['http://localhost:8000',  # The domain where Swagger UI is running
             'http://editor.swagger.io',
             'http://petstore.swagger.io']
X_HEADERS = ['Content-Type', 'If-Match']  # Needed for the "Try it out" buttons

recipe = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'recipe',
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': RECIPE_SCHEMA
}

DOMAIN = {'recipe': recipe}
