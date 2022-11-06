from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', homeview, name = 'homeview')
]