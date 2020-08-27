from django.conf import settings
from django_elasticsearch_dsl import Document,Index,fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
from product.models import Product

# @registry.register_document
# class ProductDocument(Document):
#     class Index:
#         name='hightechtn_new'
#         settings ={
#             'number_of_shards':1,
#             'number_of_replicas':1
#            }
#     id = fields.IntegerField(attr='id')    
           
#     class Django:
#         model = Product
#         fields =[
#             'id','category','description','domain','name','reference','discount','url','timestamp','brand','priceString','retailer','marketplace','seller','price','currency','sub_category','country','short_description','old_price','image','marketplaceId'
#                ]

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@INDEX.document
class ProductDocument(Document):
    """Book Elasticsearch document."""

    id = fields.TextField(
        attr='id',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    category = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    description = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    domain = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    name = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    reference = fields.KeywordField(
        analyzer=html_strip,
        fielddata=True,
        fields={
            'raw': fields.KeywordField(analyzer='keyword'),
            
        }
    )
    
    discount = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    url = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    timestamp = fields.DateField()
    
    brand = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    priceString = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    retailer = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    marketplace = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    seller = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    price = fields.FloatField()
    
    currency = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    sub_category = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    country = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    short_description = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    old_price = fields.FloatField()
    
    image = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    
    marketplaceId = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )


    class Django(object):
        """Meta options."""

        model = Product  # The model associate with this DocType
