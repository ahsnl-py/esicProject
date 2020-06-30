import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import ChatForum
from .forms import ForumForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "onlineforum/home.html", context={}, status=200)

def forum_list_view(request, *args, **kwargs):
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

def forum_create_view(request, *args, **kwargs):
    form = ForumForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'onlineforum/form.html', context={"form": form})

def forum_detail_view(request, forum_id, *args, **kwargs):
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