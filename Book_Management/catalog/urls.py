from django.urls import path
from catalog.views import *

urlpatterns = [
    path('books/', HomeView, name = 'homeview')
]