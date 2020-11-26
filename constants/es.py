import os

ES_CONNECTION_HOST = os.environ.get('ES_CONNECTION_HOST', ['localhost'])
ES_CONNECTION_TIMEOUT = os.environ.get('ES_CONNECTION_TIMOUT', 60)
