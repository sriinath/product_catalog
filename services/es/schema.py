from elasticsearch_dsl import Document, Text, Float, Boolean, Nested, Object, \
    Integer

from .index import ProductCatalogIndex

@ProductCatalogIndex.document
class Product(Document):
    product_id = Integer(required=True)
    title = Text()
    description = Text()
    in_stock = Boolean()
    price = Float()
    stock = Integer()
    image_urls = Nested()
    product_meta = Object()
