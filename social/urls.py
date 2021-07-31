from django.urls import path
from . import views


urlpatterns = [
    path('', views.social, name="social"),
    path('add_social_account/', views.add_social_account, name="add_social_account")
]
