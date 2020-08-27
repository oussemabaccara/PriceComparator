from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product,Categoryy
from search_indexes.documents import ProductDocument
from django.core.paginator import Paginator
# Create your views here.

def comparepage(request,product_id):
    obj = get_object_or_404(Product, pk=product_id)
    page = request.GET.get('page', 1)
    productlist = Product.objects.values('category')
   
    # use = Elasticsearch()
    # for i in s:
    #     if i not in use:
    #         use.index(newsearch,i)
    #         return HttpResponse(use)
    total = s.count()
    s = s[0:total]
    p=list(s)
    paginator = Paginator(p, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(12)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context ={'productspercat' : s ,'obj':obj,'products':products}
    # return HttpResponse(s)
    return render(request,'product/productscompare.html',context)



def searching(request):
    q=request.GET.get('q')
    if q :
        products = ProductDocument.search().query("match",name=q)
    else :
        products=''
    context = {'products':products}
    return render(request,'product/searching.html',context)

def index(request):
    return HttpResponse("Hello, world. You're at the product index.")

def products(request):
    return render(request,'product/products.html')

def gotocat(request):
    return render(request,'product/category.html')

def category(request):
        categorylist = Categoryy.objects.all()
        products = ProductDocument.search().sort('price')
        context = {'categorylist': categorylist,'products':products}
        return render(request,'product/category.html',context)

def productscategory(request):
    s = ProductDocument.search()
    
    categ_id=request.GET.get('category_id')
    if categ_id :
        obj = get_object_or_404(Categoryy, pk=categ_id)
        s = s.filter("match", category=obj.categoryname)
        

    s = s.sort('price')
    # client = connections.create_connection(hosts=['http://localhost:9200'])
    # s = Search(using=client, index="hightechtn_new")

    # # how simple we just past CURL code here
    # body = {
    #     "size": 0,
    #     "aggs": {
    #         "by_ref": {
    #             "terms": {
    #                 "field": "reference"
    #             }
    #         }
    #     }
    # }

    # s = Search.from_dict(body)
    # s = s.index("hightechtn_new")
    # body = s.to_dict()

    # t = s.execute()

    # for item in t.aggregations.by_ref.buckets:
    # # item.key will the house number
    #     print (item.key, item.doc_count)
    # return HttpResponse("sfqf")
    page = request.GET.get('page', 1)
    total = s.count()
    s = s[0:total]
    p=list(s)
    paginator = Paginator(p, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(12)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    categorylist = Categoryy.objects.all()
    context ={'productspercat' : s ,'products':products, 'categorylist':categorylist, 'categ_id': categ_id,}
    return render(request,'product/products.html',context)

