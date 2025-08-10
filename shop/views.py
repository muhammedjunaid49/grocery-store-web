

from django.shortcuts import render, get_object_or_404
from .models import products
from.models import *
from django.db.models import Q
# Create your views here.

def home(request, c_slug=None):
    if c_slug:
        c_page = get_object_or_404(category, slug=c_slug)
        prod = products.objects.filter(category=c_page, available=True)
    else:
        prod = products.objects.filter(available=True)

    ct = category.objects.all()

    return render(request, 'home page.html', {'pr': prod, 'ct': ct})


def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'product.html',{'pr':prod})




def searching(request):
    prod=None
    query=None

    if 'q' in request.GET:
        query = request.GET['q']
        prod=products.objects.filter().filter(Q(name__contains=query) | Q(description__contains=query))

    return render(request, 'search.html', {'qr':query,'pr':prod})



def cart_details(request):
    return render(request, 'cart.html')
