from django.http.response import HttpResponse
from django.shortcuts import render

types = {
        'stress' : ['Let Go Of Stress', '<iframe width="560" height="315" src="https://www.youtube.com/embed/c1Ndym-IsQg?start=5&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'sleep' : ['Switching Off for deep sleep', '<iframe width="560" height="315" src="https://www.youtube.com/embed/3o9etQktCpI?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'change-perspective' : ['Changing Perspective', '<iframe width="560" height="315" src="https://www.youtube.com/embed/iN6g2mr0p3Q?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'letting-go' : ['Letting Go of Effort', '<iframe width="560" height="315" src="https://www.youtube.com/embed/wyj8l9miy4w?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'dark-thoughts' : ['Understanding Dark Thoughts', '<iframe width="560" height="315" src="https://www.youtube.com/embed/L7u5N2MfTNU?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
    }

def meditate_home(request):
    return render(request, 'meditation/home.html', context= {'types' : types})

def meditate(request,type):
    try:
        return render(request, 'meditation/meditate.html', context={'video' : types[type]})

    except Exception as e:
        return HttpResponse('Never Gonna Give You Up')

