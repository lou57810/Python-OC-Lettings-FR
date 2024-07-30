# from django.http import HttpResponseNotFound
from sentry_sdk import capture_message
from django.shortcuts import render


def custom404(request, *args, **kwargs):
    capture_message("Page not found!", level="error")
    return render(request, 'error404.html')


def custom500(request, *args, **kwargs):
    capture_message("Error 500!", level="error")
    return render(request, 'error500.html')


def index(request):
    return render(request, 'lettings/home.html')
