
from django.urls import path

from . import views as user_views

app_name = 'profile'

urlpatterns = [
   # path('profile/', user_views.profile, name='profile'),
    path('<str:username>/', user_views.profile, name='profile_detail'),
]