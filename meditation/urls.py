from django.urls import path
from .views import *

urlpatterns = [
    path('', meditate_home , name='meditation_home'),
    path('<str:type>/', meditate, name='meditate')
]
