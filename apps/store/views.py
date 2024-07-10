from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages

from .models import ReceivedMessages
from apps.products.models import Produtcs

def index(request):
    products = Produtcs.objects.all()
    return render(request, 'index.html', {'products': products})


def contact_us(request):
    if request.method == 'GET':
        return render(request, 'contact_us.html')
    elif request.method == 'POST':
        name = request.POST.get('txtFullName')
        email = request.POST.get('txtEmail')
        message = request.POST.get('txtMessage')

        if len(email) == 0 or len(message) == 0:
            messages.add_message(request, constants.ERROR, 'Os campos de email e mensagem não podem estar vazios.')
            return render(request, 'contact_us.html')
        
        received_message = ReceivedMessages(
            name=name,
            email=email,
            message=message,
        )
        received_message.save()
        messages.add_message(request, constants.SUCCESS, 'Obrigado pelo feedback!!! Central de Relacionamento Quitanda Online')
        return render(request, 'contact_us.html')
