from .index import ProductCatalogIndex
from .schema import Product

def run_migrations():
    print('Started the migration')
    ProductCatalogIndex.create(ignore=[400, 404])
    Product.init()
    print('Migration is Completed')
