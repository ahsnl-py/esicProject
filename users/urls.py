
from django.urls import path

from . import views as user_views

app_name = 'profile'

urlpatterns = [
    path('edit', user_views.profile_update_view),
   # path('profile/', user_views.profile, name='profile'),
    path('<str:username>/', user_views.profile, name="profile_detail"),
]