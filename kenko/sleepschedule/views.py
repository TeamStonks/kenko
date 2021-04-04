from django.shortcuts import render

# Create your views here.
def sleep_schedule(request):
    return render(request, 'sleep-schedule/home.html')
