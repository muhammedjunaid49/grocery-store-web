

from django.contrib import admin
from . models import*
from .models import category,products
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','slug','price','stock','image')
    list_editable = ('price','stock','image')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,ProductAdmin)