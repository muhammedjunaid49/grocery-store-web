from .models import *
from .views import *

def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}

    try:
        ct = cartlist.objects.filter(cart_id=cart_id(request)).first()
        if ct:
            itc = items.objects.filter(cart=ct)
            for c in itc:
                item_count += c.quantity
    except cartlist.DoesNotExist:
        item_count = 0

    return dict(itc=item_count)
