from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'search'

    def ready(self):
        from elasticsearch_dsl import connections
        from constants.es import ES_CONNECTION_HOST, ES_CONNECTION_TIMEOUT

        connections.create_connection(
            hosts=ES_CONNECTION_HOST, timeout=ES_CONNECTION_TIMEOUT
        )
