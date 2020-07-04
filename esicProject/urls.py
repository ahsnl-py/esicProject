"""esicProject URL MAIN Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from users import views as user_views
from blog import views as dept_views
from onlineforum import views as forum_views


urlpatterns = [
    path('admin/', admin.site.urls),   
    path('home/', forum_views.forums_list_view, name='home'),
    path('forums/', forum_views.forums_list_view),
    path('<int:forum_id>', forum_views.forums_detail_view),
    path('api/forums/', include('onlineforum.api.urls')),
    path('register/', user_views.register, name='register'),
   # path('profile/', user_views.profile, name='profile'),
    path('profile/', include('users.urls', namespace='profile')),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_URL)