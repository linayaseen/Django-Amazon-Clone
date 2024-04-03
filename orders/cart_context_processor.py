from .models import Cart , CartDetail

def get_cart_data(request):
    if request.user.is_uthenticated:
        cart,created=Cart.objects.get_or_creat(request.user,status='inprogress')
        cart_detail=CartDetail.objects.filter(cart=cart)
        return{'cart_data':cart,'cart_detail_data':cart_detail}
    else:
        return{}