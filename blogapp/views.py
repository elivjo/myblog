from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BlogAuthor, Post, Comment
from django.views import generic



# Create your views here.
def index(request):
    return render(request, 'index.html',)

class BlogListView(generic.ListView):

    model = Post




