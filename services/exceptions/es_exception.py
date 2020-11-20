import json
from json.decoder import JSONDecodeError
from elasticsearch.exceptions import ConnectionError, RequestError, NotFoundError
from elasticsearch_dsl.exceptions import ValidationException
from django.http.response import JsonResponse
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_422_UNPROCESSABLE_ENTITY, \
    HTTP_500_INTERNAL_SERVER_ERROR, HTTP_503_SERVICE_UNAVAILABLE

class ExceptionHandler:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        try:
            return self.func(self, request, *args, **kwargs)
        except JSONDecodeError as exc:
            print(exc)
            return JsonResponse({
                'status': 'Failure',
                'message': 'JSON provided in request body is not valid.'
            }, status=HTTP_400_BAD_REQUEST)
        except (ValidationException, ValueError) as exc:
            print(exc)
            return JsonResponse({
                'status': 'Failure',
                'message': 'Please make sure the provided product schema is valid.'
            }, status=HTTP_400_BAD_REQUEST)
        except (RequestError, NotFoundError) as exc:
            print(exc)
            return JsonResponse({
                'status': 'Failure',
                'message': "Error connecting the ES server."
            }, status=exc.status_code)
        except ConnectionError as exc:
            print(exc)
            return JsonResponse({
                'status': 'Failure',
                'message': 'Cannot process this request at this point of time. Please try again later'
            }, status=HTTP_503_SERVICE_UNAVAILABLE)
        except AssertionError as exc:
            print(exc)
            message = str(exc)
            if not message:
                message = 'Please make sure the request is valid.'
            return JsonResponse({
                'status': 'Failure',
                'message': message
            }, status=HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as exc:
            print(exc)
            return JsonResponse({
                'status': 'Failure',
                'message': 'Something went wrong while processing the request.'
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)
