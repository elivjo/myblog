from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BlogAuthor, Post, Comment
from django.views import generic



# Create your views here.
def index(request):
    return render(request, 'index.html',)

class PostListView(generic.ListView):

    model = Post

class PostListByAuthor(generic.ListView):
    
    model = Post

    def get_target_author(self):
        
        id = self.kwargs['pk'] # variables id japim vleren e pk qe specifikuam ne URL
        target_author = get_object_or_404(BlogAuthor, pk = id) 
        return Post.objects.filter(author=target_author)
    
class PostDetailView(generic.DetailView):

    model= Post
        
class BloggerListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5
    




