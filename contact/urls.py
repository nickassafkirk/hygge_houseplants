from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path('', contactView, name='contact'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]
