from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('finance', views.finance, name='finances'),
    path('whoe', views.whoe, name='whoe'),
    path('co', views.co_financing, name='co'),
    path('cooperations', views.cooperations, name='cooperations'),
]

