from django.urls import path
from .api.product_catalog import ProductCatalog
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products', ProductCatalog.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
