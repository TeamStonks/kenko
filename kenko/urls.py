from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('workout/', include('workout.urls')),
    path('meditation/', include('meditation.urls')),
    path('sleep-schedule/', include('sleepschedule.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
