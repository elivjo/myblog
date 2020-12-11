
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name = 'index'),
   path('posts/', views.PostListView.as_view(), name='posts'),
   path('blogger/<int:pk>', views.PostListByAuthor.as_view(), name='posts-author'),
]