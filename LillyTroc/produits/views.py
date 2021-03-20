from django.shortcuts import render
from .models import Article

def produits_index(request):
	article = Article.objects.all()
	data = {'articles': article}  #bien utiliser CETTE FORMULATION
	return render(request, 'produits/produits_index.html', data)

# Create your views here.

def articles(request, name):
	return render(request, 'produits/article.html')
