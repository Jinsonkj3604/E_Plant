from django.shortcuts import get_object_or_404, render,redirect
from eplant_home.models import Product
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cartpage(request,tot = 0,count=0,cart_item=None):
    list = []
    try:
        ct = CartList.objects.get(cart_id = c_id(request))
        ct_item = CartItem.objects.filter(cart = ct,active=True)
        print(ct_item,"the objetctcttc")


        for i in ct_item:
            print(i,"each items in listttttttt")
            tot += (i.prod.price*i.quantity)
            list.append(i.prod.price)
            print(list,"eachhhhhh printed list")
            count += i.quantity

    except ObjectDoesNotExist:
        pass
    
    return render(request,'cart_page.html',{'ci':ct_item,'total':tot,'cot':count})

def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()

        # print(ct_id,"the session key is hereeeeeeeeeeeeeee####/")
    return ct_id
    
def add_cart(request,produc_id):
    product = Product.objects.get(id=produc_id)

    try:
        ct = CartList.objects.get(cart_id = c_id(request))

    except CartList.DoesNotExist:
        ct = CartList.objects.create(cart_id = c_id(request))
        ct.save()

    try:
        c_item = CartItem.objects.get(prod=product,cart=ct)
        if c_item.quantity < c_item.prod.stock:
            c_item.quantity += 1
        c_item.save()
    except CartItem.DoesNotExist:
        c_item = CartItem.objects.create(prod = product,cart=ct,quantity = 1)
        c_item.save()

    # print("the first is ct:",ct,"the c items is the here: ",c_item,)
    return redirect('cartDetails')

def minus_cart(request,produc_id):
    ct = CartList.objects.get(cart_id =c_id(request))
    prodt = get_object_or_404(Product,id=produc_id)
    c_items = CartItem.objects.get(prod=prodt, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
        
    return redirect('cartDetails')

def clear_cart(request,produc_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(Product,id=produc_id)
    c_items = CartItem.objects.get(prod=prodt, cart=ct)
    c_items.delete()

    return redirect('cartDetails')
