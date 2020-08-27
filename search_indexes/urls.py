from django.urls import path
from . import views
app_name = 'Search_indexes'

urlpatterns = [    
    path('', views.index, name='index'),
    path('categoryname',views.categoryname,name='categoryname'), 
]