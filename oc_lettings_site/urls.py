from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# from django.conf.urls import handler404
# from django.conf.urls import handler500

import time
from oc_lettings_site.views import index


def trigger_error(request):
    raise Exception("This is a test error")


def large_resource(request):
    time.sleep(4)
    return HttpResponse("Done!")


handler404 = 'oc_lettings_site.views.custom404'
handler500 = 'oc_lettings_site.views.custom500'


urlpatterns = [
    path('', index, name='home'),
    path('error/', trigger_error),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('large_resource/', large_resource),]
