from django.shortcuts import render
from .models import BlogAuthor, Post, Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.models import User



# Create your views here.
@login_required
def index(request):
    num_posts = Post.objects.all().count()
        
    num_authors = BlogAuthor.objects.count()

    context = {
        'num_posts': num_posts,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class PostListView(LoginRequiredMixin, generic.ListView):

    model = Post



class PostListByAuthorView(LoginRequiredMixin, generic.ListView):
    
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
        
class BloggerListView(LoginRequiredMixin, generic.ListView):
    model = BlogAuthor
    


class PostCommentCreateView(LoginRequiredMixin, CreateView):
   
    model = Comment
    fields = ['comment',]
    

    def get_context_data(self, **kwargs):
        """ shtimi i te dhenave te nje posti ne templatin comment_form.html """
        
        context = super(PostCommentCreateView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """ lidhja e autorit me postin """
       
        form.instance.author = self.request.user  #vendosja e nje useri si autor i komentit
        form.instance.blog = get_object_or_404(Post, pk = self.kwargs['pk'])  # lidhja e komentit me postin
        return super(PostCommentCreateView, self).form_valid(form)

    def get_success_url(self): 
        """ kthimi ne url specifike mbas postimit te komentit """
        
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})





