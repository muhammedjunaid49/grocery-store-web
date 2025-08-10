
from django.shortcuts import render,redirect,get_object_or_404
from cart.models import cartlist, items
from shop.models import products

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart_details(request,total=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=cart_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            total+=(i.product.price*i.quantity)
            count+=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html',{'ct':ct_items,'total':total,'count':count})
def cart_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        request.session.create()  # Creates a new session and assigns an ID
        ct_id = request.session.session_key
    return ct_id


def add_cart(request, product_id):
    prod = products.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=cart_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=cart_id(request))
        ct.save()

    # ✅ Get quantity from request (default to 1)
    try:
        quantity = int(request.GET.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1

    try:
        c_items = items.objects.get(product=prod, cart=ct)
        if c_items.quantity + quantity <= c_items.product.stock:
            c_items.quantity += quantity
        else:
            c_items.quantity = c_items.product.stock
        c_items.save()
    except items.DoesNotExist:
        if quantity > prod.stock:
            quantity = prod.stock
        c_items = items.objects.create(product=prod, quantity=quantity, cart=ct)
        c_items.save()

    return redirect('CartDetails')


def min_cart(request, product_id):
    ct=cartlist.objects.get(cart_id=cart_id(request))
    product=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(product=product,cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('CartDetails')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(products, id=product_id )
    c_items = items.objects.get(product=product, cart=ct)
    c_items.delete()
    return redirect('CartDetails')
