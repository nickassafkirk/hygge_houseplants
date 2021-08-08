from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, Variant


def view_car(request):
    return render(request, 'cart/car.html')
