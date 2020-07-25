from django.urls import path
from blog.views import Blog
from . import views
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),


    path('blog/',views.blog_list , name = 'blog_list') ,
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]