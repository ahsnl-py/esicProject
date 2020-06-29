
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from .models import Forum 
from .forms import ForumForm
from .serializers import ForumSerializer
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'forum/home.html', context={}, status=200)

def forum_create_view(request, *args, **kwargs):
    serializer = ForumSerializer(data=request.POST or None)
    if serializer.is_valid():
        obj = serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({}, status=400)