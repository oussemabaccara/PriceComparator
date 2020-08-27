from django.urls import path
from . import views
app_name = 'Product'

urlpatterns = [ 
    path('comparepage/<str:product_id>',views.comparepage,name='comparepage'),
    path('searching',views.searching,name='searching'),
    path('products',views.productscategory,name='products'),
    path('', views.index, name='index'),
    path('category',views.category,name='category'),   
]