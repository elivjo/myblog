
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name = 'index'),
   path('posts/', views.PostListView.as_view(), name='posts'),
   path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
   path('post/<int:pk>/comment/', views.PostCommentCreateView.as_view(), name='post_comment'),
   path('post/<int:pk>/report/', views.PostReportCreateView.as_view(), name='post_report'),
   path('blogger/<int:pk>', views.PostListByAuthorView.as_view(), name='posts-author'),
   path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
   path('like/<int:pk>', views.LikeView, name='like_post'),
    
]