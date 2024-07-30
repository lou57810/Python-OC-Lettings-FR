from django.urls import path
# import profiles.views
from . import views


urlpatterns = [
    path('index/', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
