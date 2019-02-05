from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'newsfeed/', views.post_list, name='post_list'),
    path(r'post/<pk>/', views.post_detail, name='post_detail'),
    path(r'post_new', views.post_new, name='post_new'),
    path(r'post/<pk>/edit/', views.post_edit, name='post_edit'),
    path(r'post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'drafts/', views.post_draft_list, name='post_draft_list'),
    path(r'post/<pk>/publish/', views.post_publish, name='post_publish'),
    path(r'post/<pk>/remove/', views.post_remove, name='post_remove'),
    path(r'map/', views.map, name='map'),
]