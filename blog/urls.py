from django.urls import path
from .import views
from users import views as user_views

app_name = 'blog'
urlpatterns = [
    # blog/department
    path('', views.departments, name='departments'),
    # blog/<single_slug>
    path('<single_slug>', views.single_slug, name='single_slug'),
    # /post_list views
    path('post_list/', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
] 