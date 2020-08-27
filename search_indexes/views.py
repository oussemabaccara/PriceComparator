from django.shortcuts import render
from django.http import HttpResponse
from search_indexes.documents import ProductDocument
# Create your views here.

def index(request):
    products = ProductDocument.search().query('match', category='Home')
    for product in products:
        return HttpResponse(product.name)


def categoryname(request):
        products = ProductDocument.search().query('match', category='Home')
        # output = ', '.join([q for q in productlist])
        context = {'products': products}
        return render(request,'product/category.html',context)