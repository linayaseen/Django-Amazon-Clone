from django.shortcuts import render ,redirect
from django.shortcuts import get_object_or_404
import datetime

from .models import Order,OrderDetail,Cart,CartDetail,Coupon
from products.models  import Product
from settings.models import DeliveryFee

def order_list(request):
    data=Order.objects.filter(user=request.user)#.all()#.order_by('price')#filter(use__id=1)
    return render(request,'orders/order_list.html',{'orders':data})
    '''
    data = Order.objects.all() #queryset cache
    data2=data.objects.filter(price__gt=30)
    '''
    
def checkout(request):
    cart=Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail=CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    
    
    if request.method == 'POST':
        code=request.POST['copoun_code']
       # coupon=Coupon.objects.get(code=code)
        coupon=get_object_or_404(Coupon , code=code)
        
        if coupon and coupon.quantity > 0:
            today_date=datetime.datetime.today(0).date()
            if today_date >=coupon.start_date and today_date <= coupon.end_date:
                coupon_value=round(cart.cart_total / 100*coupon.discount,2)
                sub_total=cart.cart_total - coupon_value
                total=sub_total+delivery_fee
                
                cart.coupon=coupon
                cart.total_with_coupon=sub_total
                cart.save()
                
                coupon.quantity-=1
                coupon.save()
                
                
                
                return render(request,'orders/checkout.html',{
                    'cart_detail': cart_detail,
                    'delivery_fee': delivery_fee,
                    'sub_total':sub_total,
                    'discount':discount,
                    'total':total
        
    })
                
                
    
    sub_total=cart.cart_total
    discount=0
    total=sub_total+delivery_fee
    return render(request,'orders/checkout.html',{
        'cart_detail': cart_detail,
        'delivery_fee': delivery_fee,
        'sub_total':sub_total,
        'discount':discount,
        'total':total
        
    })


def add_to_cart(request):
    product= Product.objects.get(id=request.POST['product_id'])
    quantity= int(request.POST['quantity'])
    
    cart = Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail,created=CartDetail.objects.get_or_create(cart=cart,product=product)
    '''
    if not created:
        cart_detail.quantity=cart_detail.quantity+quantity
    '''
    cart_detail.quantity=quantity
    cart_detail.total= round(product.price* cart_detail.quantity,2)
    cart_detail.save(f'/products/{product.slug}')