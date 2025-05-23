"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.reverse import reverse
from .views import UserView, TeamView, ActivityView, LeaderboardView, WorkoutView

def api_root(request):
    return JsonResponse({
        "users": reverse('users', request=request),
        "teams": reverse('teams', request=request),
        "activity": reverse('activity', request=request),
        "leaderboard": reverse('leaderboard', request=request),
        "workouts": reverse('workouts', request=request),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserView.as_view(), name='users'),
    path('api/teams/', TeamView.as_view(), name='teams'),
    path('api/activity/', ActivityView.as_view(), name='activity'),
    path('api/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('api/workouts/', WorkoutView.as_view(), name='workouts'),
    path('', api_root, name='api_root'),
]
