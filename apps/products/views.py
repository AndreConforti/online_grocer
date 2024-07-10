from django.shortcuts import render
from .models import Produtcs

def product_details(request, id):
    product = Produtcs.objects.get(id=id)
    return render(request, 'product_details.html', {'product': product})