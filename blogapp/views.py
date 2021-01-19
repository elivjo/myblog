from django.shortcuts import render
from .models import BlogAuthor, Post, Comment, PostReport
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post.id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args= [str(pk)]))

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

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)


        post= get_object_or_404(Post, pk = self.kwargs['pk'])
        total_likes= post.total_likes()

        liked= False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes']= total_likes
        context['liked']= liked
        return context


        
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

    def get_success_url(self, *args): 
        """ kthimi ne url specifike mbas postimit te komentit """
    
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})
   

class PostReportCreateView(LoginRequiredMixin, CreateView):
   
    model = PostReport
    fields = ['comment_report',]
    

    def get_context_data(self, **kwargs):
        """ shtimi i te dhenave te nje posti ne templatin comment_form.html """
        
        context = super(PostReportCreateView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        
        return context
        
    def form_valid(self, form):
        """ lidhja e autorit me postin """
       
        form.instance.author = self.request.user  #vendosja e nje useri si autor i komentit
        form.instance.blog_report = get_object_or_404(Post, pk = self.kwargs['pk'])  # lidhja e komentit me postin
        return super(PostReportCreateView, self).form_valid(form)



    def get_success_url(self, *args): 
        """ kthimi ne url specifike mbas postimit te komentit """
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})
        
        



