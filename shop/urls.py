from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart_details, name='cartDetails'),  # Specific first
    path('search/', views.searching, name='search'),         # Specific before slug routes
    path('<slug:c_slug>/', views.home, name='prod_cat'),     # Catch-all last
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetails, name='details'),
]
