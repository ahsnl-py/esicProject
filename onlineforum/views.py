import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ChatForum
from .forms import ForumForm
from .serializers import ChatForumSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "onlineforum/home.html", context={}, status=200)

"""List View"""
@api_view(['GET'])
def forum_list_view(request, *args, **kwargs):
    qs = ChatForum.objects.all()
    serializer = ChatForumSerializer(qs, many=True)
    return Response(serializer.data, status=200)

"""Detail View"""
@api_view(['GET'])
def forum_detail_view(request, forum_id, *args, **kwargs):
    qs = ChatForum.objects.filter(id=forum_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ChatForumSerializer(obj)
    return Response(serializer.data, status=200)

"""Create View"""
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # REST API course
def forum_create_view(request, *args, **kwargs):
    serializer = ChatForumSerializer(data=request.POST or None )
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def forum_delete_view(request, forum_id, *args, **kwargs):
    qs = ChatForum.objects.filter(id=forum_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You cannot delete this forum"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "forum removed"}, status=200)




####

"""PURE DJANGO"""
def forum_create_view_pure_django(request, *args, **kwargs):
    user = request.user
    if not request.user.is_authenticated:
        user = None 
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = ForumForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.user = user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'onlineforum/form.html', context={"form": form})

def forum_list_view_pure_django(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Andriod
    return json data
    """
    qs = ChatForum.objects.all()
    forum_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": forum_list
    }
    return JsonResponse(data)

def forum_detail_view_pure_django(request, forum_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Andriod
    return json data
    """
    data = {
        "id": forum_id,
    }
    status = 200
    try:
        obj = ChatForum.objects.get(id=forum_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status) # json.dumps content_type='application/json'