from django.shortcuts import render

# Create your views here.
def sleep_schedule(req):
    return render(req, 'sleep-schedule/home.html')
