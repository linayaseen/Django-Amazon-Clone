from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Product,Brand,Review ,ProductImages


class ProductList(ListView):
    model=Product
    
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
        return context
    
