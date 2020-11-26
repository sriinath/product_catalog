import json
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from services.exceptions.es_exception import ExceptionHandler
from services.es.schema import Product

class ProductCatalog(APIView):
    @ExceptionHandler
    def post(self, req):
        payload = json.loads(req.body)
        product = Product(**payload)
        product.save()
        product_data = product.to_dict(include_meta=True)
        return JsonResponse(dict(
            status="Success",
            data=dict(
                **product_data.get('_source', {}),
                _id=product_data.get('_id', None)
            )
        ), status=HTTP_200_OK)

    @ExceptionHandler
    def get(self, req):
        page = req.GET.get('page', 1)
        limit = req.GET.get('limit', 25)
        title = req.GET.get('title', '')
        start_index = (page - 1) * limit
        end_index = start_index + limit

        search = Product.search().query(
            "match", title=title
        )[start_index: end_index]

        search = search.execute().to_dict()
        search_data = search.get('hits', {}).get('hits', [])
        count = search.get('hits', {}).get('total', {}).get('value', 0)

        result = list()
        for data in search_data:
            result.append(data.get('_source', {}))

        return JsonResponse({
            "data": result,
            "total_count": count
        }, status=HTTP_200_OK)
