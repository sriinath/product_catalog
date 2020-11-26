from django.urls import path
from .api.product_catalog import ProductCatalog
from .api.search import Search
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', Search.as_view()),
    path('products', ProductCatalog.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
