from django.contrib import admin
from .models import Product,Categoryy

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['timestamp']

admin.site.register(Product,ProductAdmin)
admin.site.register(Categoryy)



