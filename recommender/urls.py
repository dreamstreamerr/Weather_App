from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend_drink, name='recommend_drink'),
    path('drink/<slug:slug>/', views.drink_detail, name='drink_detail'),
]
