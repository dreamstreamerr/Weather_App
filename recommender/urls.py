from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend_drink, name='recommend_drink'),
]
