from django.shortcuts import render
from django.views.generic import View


class BeginnerWorkoutView(View):
    def get(self, request):
        return render(request, 'beginner-workout.html')


class IntermediateWorkoutView(View):
    def get(self, request):
        return render(request, 'intermediate-workout.html')


class AdvancedWorkoutView(View):
    def get(self, request):
        return render(request, 'advanced-workout.html')
