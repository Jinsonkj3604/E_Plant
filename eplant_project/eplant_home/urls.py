from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('details',views.productitem,name='details'),
     path('search',views.search,name='search'),
    path('<slug:c_slug>',views.home,name='slug'),
    path('<slug:c_slug>/<slug:prod_slug>/',views.productitem,name='ProdDetail'),
   
    

]
