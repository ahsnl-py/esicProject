import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Forum 
from .forms import ForumForm
from .serializers import (
    ForumSerializer, 
    ForumActionSerializer,
    ForumCreateSerializer
)

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

""""Home View"""
def home_view(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "forum/home.html", context={"username": username}, status=200)
    


"""Create View"""
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # REST API course
def forum_create_view(request, *args, **kwargs):
    serializer = ForumSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


"""Detail View"""
@api_view(['GET'])
def forum_detail_view(request, forum_id, *args, **kwargs):
    qs = Forum.objects.filter(id=forum_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ForumSerializer(obj)
    return Response(serializer.data, status=200)


"""Delete View"""
@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def forum_delete_view(request, forum_id, *args, **kwargs):
    qs = Forum.objects.filter(id=forum_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You cannot delete this forum"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "forum removed"}, status=200)


"""
Action View
Action options : [like, unlike, repost]
"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def forum_action_view(request, forum_id, *args, **kwargs):
    
    serializer = ForumActionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        forum_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
        qs = Forum.objects.filter(id=forum_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = ForumSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = ForumSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "repost":
            new_forum = Forum.objects.create(
                    user=request.user, 
                    parent=obj,
                    content=content,
                    )
            serializer = ForumSerializer(new_forum)
            return Response(serializer.data, status=200)
    return Response({}, status=200)


"""List View"""
@api_view(['GET'])
def forum_list_view(request, *args, **kwargs):
    qs = Forum.objects.all()
    serializer = ForumSerializer(qs, many=True)
    return Response(serializer.data, status=200)
