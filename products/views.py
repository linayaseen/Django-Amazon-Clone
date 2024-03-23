from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Product,Brand,Review ,ProductImages


class ProductList(ListView):
    model=Product
    paginate_by = 50
    
#context{},queryset: product.object.all(): 1:option 2:method :override
#queryset: main data :datail product 
#context: extra data :reviews, images

#queryset:[products] :filter
#context: user
    
class ProductDetail(DetailView): 
    model=Product
    
    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context["reviews"]= Review.objects.filter(product=self.get_object())
        context["images"]= ProductImages.objects.filter(product=self.get_object())
        context["related"]= Product.objects.filter(brand=self.get_object().brand)[:10]
        return context
    
class BrandList(ListView):
    model=Brand 
    paginate_by = 50
    

class BrandDetail(ListView):
    model=Product 
    template_name='products/brand_detail.html'
    paginate_by = 50
    
    def get_context_data(self) :
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"]= Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
         
'''
class BrandDetail(DetailView):
    model=Brand 
    
    def get_context_data(self, **kwargs: Any) :
        context = super().get_context_data(**kwargs)
        context["products"]= Product.objects.filter(brand=self.get_object())
        return context
    
'''