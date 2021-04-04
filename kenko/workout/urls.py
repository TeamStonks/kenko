from django.urls import path
from .views import *

urlpatterns = [
    path('beginner-workout', BeginnerWorkoutView.as_view(), name="workout"),
    path('intermediate-workout', IntermediateWorkoutView.as_view(), name="workout"),
    path('advanced-workout', AdvancedWorkoutView.as_view(), name="workout"),
]
