from . import views
from django.urls import path

urlpatterns = [
    path('cartDetails',views.cartpage,name='cartDetails'),
    path('add/<int:produc_id>/',views.add_cart,name='addcart'),
    path('dec/<int:produc_id>/',views.minus_cart,name='cart_decrement'),
    path('clr/<int:produc_id>/',views.clear_cart,name='remove_cart'),

]