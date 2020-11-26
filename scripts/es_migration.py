import os
import sys
from elasticsearch_dsl import connections
from elasticsearch.exceptions import ConnectionError
sys.path.append(os.getcwd())

from services.es.create_mapping import run_migrations
from constants.es import ES_CONNECTION_HOST, ES_CONNECTION_TIMEOUT

connections.create_connection(
    hosts=ES_CONNECTION_HOST, timeout=ES_CONNECTION_TIMEOUT
)

if __name__ == '__main__':
    try:
        run_migrations()
    except ConnectionError as err:
        print("Error while trying to connect to ES server. Make sure ES server is up and running.")
        print(err)
