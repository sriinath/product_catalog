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
        title = req.GET.get('title', '')
        search = Product.search().query(
            "match", title=title
        )
        search = search.execute()
        print(search)
        return JsonResponse({
            "status": "Success"
        }, status=HTTP_200_OK)
