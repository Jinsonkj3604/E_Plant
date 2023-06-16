from django.contrib import admin
from . models import *


# Register your models here.
class shopadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']


admin.site.register(Shop,shopadmin)

class productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','price','stock','image']
    list_editable = ['price','stock','image']
admin.site.register(Product,productadmin)
