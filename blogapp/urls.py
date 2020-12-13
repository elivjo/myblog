
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name = 'index'),
   path('posts/', views.PostListView.as_view(), name='posts'),
   path('blogger/<int:pk>', views.PostListByAuthorView.as_view(), name='posts-author'),
   path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
   path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
]