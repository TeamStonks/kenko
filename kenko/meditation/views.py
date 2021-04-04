from django.http.response import HttpResponse
from django.shortcuts import render

types = {
        'stress' : ['Let Go Of Stress', 'An easy meditation exercise to let go off stress and relax the brain and body.', '<iframe width="1120" height="630" src="https://www.youtube.com/embed/c1Ndym-IsQg?start=5&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'sleep' : ['Switching off for deep sleep', 'Unable to sleep? This meditation exercise calms the brain and helps you fight insomnia and doze off.','<iframe width="1120" height="630" src="https://www.youtube.com/embed/3o9etQktCpI?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'change-perspective' : ['Changing Perspective', 'Have a different perspective to everything in your surroundings.','<iframe width="1120" height="630" src="https://www.youtube.com/embed/iN6g2mr0p3Q?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'letting-go' : ['Letting Go of Effort', 'Sometimes putting in less effort is beneficial. This meditation exercise teaches you the art of letting go.','<iframe width="1120" height="630" src="https://www.youtube.com/embed/wyj8l9miy4w?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'],
        'dark-thoughts' : ['Understanding Dark Thoughts', 'Fight dark thoughts and lead towards positivity.','<iframe width="1120" height="630" src="https://www.youtube.com/embed/L7u5N2MfTNU?&autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
    }

def meditate_home(request):
    return render(request, 'meditation/home.html', context= {'types' : types})

def meditate(request,type):
    try:
        return render(request, 'meditation/meditate.html', context={'video' : types[type]})

    except Exception as e:
        return HttpResponse('Never Gonna Give You Up')

