"""esicProject URL MAIN Configuration"""


from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin

from users import views as user_views
from blog import views as dept_views
from onlineforum import views as forum_views


urlpatterns = [
    path('admin/', admin.site.urls),   
    path('home/', forum_views.home_view, name='home'),
    path('home/forums/', forum_views.forum_list_view),
    #path('home/forum-create/', forum_views.forum_create_view),
    #path('home/forum/<int:forum_id>', forum_views.forum_detail_view),
    #path('home/api/forum/action/', forum_views.forum_action_view),
    #path('home/api/forum/<int:forum_id>/delete', forum_views.forum_delete_view),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls', namespace='blog')),
]
