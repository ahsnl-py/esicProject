from django.urls import path

from .views import (
    home_view, 
    forum_action_view,
    forum_delete_view,
    forum_detail_view, 
    forum_list_view,
    forum_create_view,
)
'''
CLIENT
Base ENDPOINT /api/forums/
'''
urlpatterns = [
    path('', forum_list_view),
    path('action/', forum_action_view),
    path('create/', forum_create_view),
    path('<int:forum_id>/', forum_detail_view),
    path('<int:forum_id>/delete/', forum_delete_view),
]