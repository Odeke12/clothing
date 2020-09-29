from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView, 
    UserPostListView
)
from . import views

urlpatterns = [ 
    path('', PostListView.as_view(), name='blog-home'), #.as_view() converts the class based view into a view
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #pk coz thats what the detail view expects
     path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
     path('about/', views.about, name='blog-about')   
]  
  
# <app>/<model>_<viewtype.html>