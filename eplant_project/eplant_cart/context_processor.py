from . models import *
from . views import *

def count(request):
    item_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            ct = CartList.objects.filter(cart_id = c_id(request))
            ctitem = CartItem.objects.all().filter(cart = ct[:1])
            for c in ctitem:
                item_count =+ c.quantity

        except CartList.DoesNotExist:
            item_count = 0

    return dict(itc = item_count)
        
