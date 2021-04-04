from django.urls import path
from .views import *

urlpatterns = [
    path('', sleep_schedule , name='sleepschedule_home'),
]