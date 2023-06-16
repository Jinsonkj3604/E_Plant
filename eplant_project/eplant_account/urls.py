from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('sign',views.usersign,name='sign'),
    path('signout',views.signout,name='signout'),
   
    ]