from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
from sentry_sdk import capture_message, capture_exception, set_tag
# from django.conf.urls import handler404, handler500


import time
from oc_lettings_site.views import index


# def trigger_error(request):
# raise Exception("This is a test error")


def large_resource(request):
    time.sleep(4)
    return HttpResponse("Done!")


def trigger_error(request):
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        set_tag("Opération non permise!")
        capture_exception(e)



urlpatterns = [
    path('', index, name='home'),
    path('sentry-debug/', trigger_error),
    path('error/', views.custom500, name='oc_lettings_error'),
    path('error', views.custom500, name='oc_lettings_error'),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('large_resource/', large_resource),]

handler404 = 'oc_lettings_site.views.custom404'
handler500 = 'oc_lettings_site.views.custom500'
