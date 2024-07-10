from django.contrib import admin
from .models import Produtcs


class ListingProducts(admin.ModelAdmin):
    list_display = ['id', 'name', 'stock', 'purchase_price', 'sale_price']
    list_display_links = ['id', 'name']
    list_per_page = 10
    list_editable = ['stock']


admin.site.register(Produtcs, ListingProducts)