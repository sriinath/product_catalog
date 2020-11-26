from elasticsearch_dsl import Index

from constants.index import PRODUCT_CATALOG_INDEX

ProductCatalogIndex = Index(
    PRODUCT_CATALOG_INDEX
)
