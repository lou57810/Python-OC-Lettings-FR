from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views


import time
from oc_lettings_site.views import index


def large_resource(request):
    time.sleep(4)
    return HttpResponse("Done!")


urlpatterns = [
    path('', index, name='home'),
    path('error/', views.custom500, name='oc_lettings_error'),
    path('error', views.custom500, name='oc_lettings_error'),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('large_resource/', large_resource),]

handler404 = 'oc_lettings_site.views.custom404'
handler500 = 'oc_lettings_site.views.custom500'
