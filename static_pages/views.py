from django.shortcuts import render


def about_us(request):
    return render(request, 'about_us.html')


def exchanges_and_returns(request):
    return render(request, 'exchanges_and_returns.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_of_use(request):
    return render(request, 'terms_of_use.html')