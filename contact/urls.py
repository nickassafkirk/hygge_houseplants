from django.urls import path

from .views import contact_view, contact_success

urlpatterns = [
    path('', contact_view, name='contact'),
    path('contact/', contact_view, name='contact_view'),
    path('success/', contact_success, name='contact_success'),
]
