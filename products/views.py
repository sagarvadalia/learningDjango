from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer

# Create your views here.


def index(req):
    products = Product.objects.all()

    return render(req, 'index.html', {'products': products})


def newViews(req):
    return HttpResponse('<h3> <b>Hello New Page</h3>')
