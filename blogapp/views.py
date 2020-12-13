from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BlogAuthor, Post, Comment
from django.views import generic
from django.shortcuts import get_object_or_404




# Create your views here.
def index(request):
    num_posts = Post.objects.all().count()
        
    num_authors = BlogAuthor.objects.count()

    context = {
        'num_posts': num_posts,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class PostListView(generic.ListView):

    model = Post



class PostListByAuthorView(generic.ListView):
    
    model = Post
    template_name ='blogapp/post_list_by_author.html'
    
     #metodat override: get_queryset dhe get_context_data
    def get_queryset(self):
        """lista e posteve nga nje autor"""
        
        id = self.kwargs['pk']
        target_author=get_object_or_404(BlogAuthor, pk = id)
        return Post.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        """ shtimi i te dhenave te autorit """
        
        context = super(PostListByAuthorView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
        return context
    


class PostDetailView(generic.DetailView):

    model= Post
        
class BloggerListView(generic.ListView):
    model = BlogAuthor
    





