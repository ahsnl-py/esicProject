import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.
def home_view(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "onlineforum/home.html", 
                        context={"username": username}, 
                        status=200)

def forums_list_view(request, *args, **kwargs):
    return render(request, "onlineforum/forum/list_forum.html")

def forums_detail_view(request, forum_id, *args, **kwargs):
    return render(request, "onlineforum/forum/detail_forum.html", context={"forum_id": forum_id})

def forums_profile_view(request, username, *args, **kwargs):
    return render(request, "onlineforum/forum/profile.html", context={"profile_username": username})
