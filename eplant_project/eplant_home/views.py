from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage
# Create your views here.
def home(request,c_slug= None):
    c_page = None
    prod_list = None
    if c_slug != None:
        c_page = get_object_or_404(Shop,slug = c_slug)
        prod_list = Product.objects.filter(category=c_page,avail=True)
    else:
        prod_list = Product.objects.all().filter(avail=True)
        paginator = Paginator(prod_list,3)
        
        try:
            page = int(request.GET.get('page','1'))
        except:
            page = 1

        try:
            prod = paginator.page(page)
        except (EmptyPage,InvalidPage):
            prod = paginator.page(paginator.num_pages)

    cat = Shop.objects.all()
    print(c_page)

    
    return render(request,'index.html',{'pr':prod, 'ct':cat})

def productitem(request,c_slug,prod_slug):
    try:
        prod= Product.objects.get(category__slug =c_slug, slug =prod_slug)
    except:
        raise Exception
    
    return render(request,'items_page.html',{'prod':prod})

def search(request):
    prod = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Product.objects.all().filter(Q(name__contains = query) | Q(desc__contains = query))
    return render(request,'search_field.html',{'pr':prod, 'qr':query})

