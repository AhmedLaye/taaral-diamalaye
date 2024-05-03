# collector/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.taaral, name='taaral'),
    # Ajoutez d'autres URL selon vos besoins
]
