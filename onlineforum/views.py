
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import ChatForum
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
    forum_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        "response": forum_list
    }
    return JsonResponse(data)


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