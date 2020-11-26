import json
from elasticsearch import Elasticsearch
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from services.exceptions.es_exception import ExceptionHandler

client = Elasticsearch()

class Search(APIView):
    @ExceptionHandler
    def get(self, req):
        index = req.headers.get('index', '')
        skip_es_info = json.loads(req.GET.get('skip_es_info', 'true'))
        body = json.loads(req.GET.get('query', '{}'))
        result = client.search(
            index=index,
            body=body
        )
        response = {"data": result.get('hits', {}).get('hits', {})} if skip_es_info else result
        return JsonResponse(response, status=HTTP_200_OK)
