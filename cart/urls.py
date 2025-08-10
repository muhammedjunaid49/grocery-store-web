from django.urls import path
from . import views


urlpatterns = [

    # ✅ Better: all lowercase URL

    path('', views.cart_details, name='CartDetails'),
    path('add/<int:product_id>/', views.add_cart, name='AddCart'),
    path('cart_decrement/<int:product_id>/', views.min_cart, name='Cart_decrement'),
    path('remove/<int:product_id>/', views.cart_delete, name='remove'),

]