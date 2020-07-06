from django.urls import path

from users import views as user_views
from .import views
from .views import (
    #PostCreateView, 
    PostDetailView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView
)

app_name = 'blog'
urlpatterns = [
    path('', views.departments, name='departments'),
    path('<single_slug>', views.single_slug, name='single_slug'),
    path('allpost/', views.post_list, name='post_list'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_view'),
    #path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         #views.post_detail,
         #name='post_detail'),
] 