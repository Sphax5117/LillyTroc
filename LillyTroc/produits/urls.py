from django.urls import path
from . import views

urlpatterns = [
    path('', views.produits_index, name='produits_index'),
    path('article/<str:name>/', views.articles, name='article'),
]

