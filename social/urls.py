from django.urls import path
from . import views


urlpatterns = [
    path('', views.edit_social_account, name="edit_social_account"),
    path('add_icon/', views.add_icon, name="add_icon"),
]
