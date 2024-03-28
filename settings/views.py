from django.shortcuts import render
from django.db.models import Count
from products.models import Product,Brand,Review

# Create your views here.
def home(request):
    new_products=Product.objects.filter(falg='New')[:10]
    sale_products=Product.objects.filter(falg='Sale')[:10]
    feature_products=Product.objects.filter(falg='Feature')[:6]
    brands=Brand.objects.annotate(Product_count=Count('product_brand'))[10]
    reviews=Review.objects.all()
    return render(request,'settings/home.html',{
        'new_products':new_products,
        'sale_products':sale_products,
        'feature_products':feature_products,
        'brands':brands,
        'reviews':reviews
    })