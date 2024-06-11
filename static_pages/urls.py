from django.urls import path
from . import views


urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('exchanges_and_returns/', views.exchanges_and_returns, name='exchanges_and_returns'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
]

