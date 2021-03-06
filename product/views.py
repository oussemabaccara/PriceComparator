from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, Q,A
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product,Categoryy
from search_indexes.documents import ProductDocument
from django.core.paginator import Paginator
# Create your views here.

def comparepage(request,product_id):
    categ_id=request.GET.get('category_id')
    obj = get_object_or_404(Product, pk=product_id)
    page = request.GET.get('page', 1)
    productlist = Product.objects.values('category')
    s = ProductDocument.search()
    s = s.filter("match", reference=obj.reference)
   
    # use = Elasticsearch()
    # for i in s:
    #     if i not in use:
    #         use.index(newsearch,i)
    #         return HttpResponse(use)
    total = s.count()
    s = s[0:total]
    p=list(s)
    # okok
    paginator = Paginator(p, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(12)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    categorylist = Categoryy.objects.all()
    context ={'productspercat' : s ,'obj':obj,'products':products,'categorylist':categorylist, 'categ_id': categ_id,}
    # return HttpResponse(s)
    return render(request,'product/productscompare.html',context)



def searching(request):
    q=request.GET.get('q')
    if q :
        products = ProductDocument.search().query("match",name=q)
        response = products.execute()
        
    else :
        products=''
    context = {'products':products,'response':response}
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
        context = {'categorylist': categorylist}
        return render(request,'product/category.html',context)

def productscategory(request):
    s = ProductDocument.search()
    # qs = s.to_queryset()
    # a = A('terms', field='reference') 
    # r = s.aggs.bucket('reference_terms',a)
    # return HttpResponse(qs)
    # v = r.metric('min_price','min',field='price')
    categ_id=request.GET.get('category_id')
    if categ_id :
        obj = get_object_or_404(Categoryy, pk=categ_id)
        s = s.filter("match", category=obj.categoryname)
        s = s.sort('price')
        qs = s.to_queryset()
        l = list(qs)
        output = []
        output2= []
        for x in l:
            if x.reference not in output:
                output.append(x.reference)
                output2.append(x)
        
        # q=0
        # a=[(l[1])]
        # for u in range(len(l)-1):
        #     while q <= (len(a)-1):
        #         if l[u].reference==a[q].reference:
        #             q=len(a)-1
        #         else :
        #             a.append(l[u])
        #             q=q+1
        
         
    
    page = request.GET.get('page', 1)
    # total = output2.count()
    # s = s[0:total]
    # p=list(s)
    paginator = Paginator(output2, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(12)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    categorylist = Categoryy.objects.all()
    context ={'productspercat' : output2 ,'products':products, 'categorylist':categorylist, 'categ_id': categ_id,}
    return render(request,'product/products.html',context)

