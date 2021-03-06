from django.shortcuts import render
from django.views.generic import View


class BeginnerWorkoutView(View):
    def get(self, request):
        return render(request, 'workout/beginner-workout.html')


class IntermediateWorkoutView(View):
    def get(self, request):
        return render(request, 'workout/intermediate-workout.html')


class AdvancedWorkoutView(View):
    def get(self, request):
        return render(request, 'workout/advanced-workout.html')
