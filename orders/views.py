from django.shortcuts import render

from .models import Order

def order_list(request):
    data=Order.objects.filter(user=request.user)#.all()#.order_by('price')#filter(use__id=1)
    return render(request,'orders/order_list.html',{'orders':data})
    '''
    data = Order.objects.all() #queryset cache
    data2=data.objects.filter(price__gt=30)
    '''
    
def checkout(request):
    return render(request,'orders/checkout.html',{})