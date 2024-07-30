# import logging
from django.shortcuts import render
from .models import Profile
from sentry_sdk import capture_exception, set_tag

# from django.http import HttpResponseNotFound
# from sentry_sdk import capture_message

"""
def my_custom_page_not_found_view(*args, **kwargs):
    capture_message("Page not found!", level="error")

    # return any response here, e.g.:
    return HttpResponseNotFound("Not found")
"""


# Create your views here.
# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
# def profiles_index(request):


def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males

def profile(request, username):
    try:
        print('user:', username)
        profile = Profile.objects.get(user__username=username)
    except Exception as e:
        # Alternatively the argument can be omitted

        set_tag("profile", f"L'utilisateur {request.user} a consulter un profil: {username} inexistant!")
        capture_exception(e)
        return render(request, 'error404.html')

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
