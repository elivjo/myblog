from django.shortcuts import render
from .models import BlogAuthor, Post, Comment, PostReport, Like
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post.id'))
    liked = False
    
    if like := post.like.filter(user__id=request.user.id):
        like.delete()
        liked = False
    else:
        like = {
            'user':  request.user,
            'action_object': post,
        }
        Like.objects.create(**like)
        #post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args= [str(pk)]))



@login_required
def index(request):
    num_posts_unbanned = Post.objects.filter(is_banned=False).count()
    #num_posts_banned = Post.objects.filter(is_banned=True).count()

    num_authors = BlogAuthor.objects.count()
    

    context = {
        'num_posts': num_posts_unbanned,
        'num_authors': num_authors,
        #'num_authors': num_posts_banned,
    }

    return render(request, 'index.html', context=context)
    

class PostListView(LoginRequiredMixin, generic.ListView):

    model = Post
    #queryset = Post.objects.filter(is_banned=False)

    
    def get_queryset(self):
        
        return Post.objects.annotate(like_count=Count('like')).order_by('-like_count').filter(is_banned= False)
    

class PostListByAuthorView(LoginRequiredMixin, generic.ListView):
    
    model = Post
    template_name ='blogapp/post_list_by_author.html'
    
    #metodat override: get_queryset dhe get_context_data
    
    def get_queryset(self):
        """lista e posteve nga nje autor"""
        
        id = self.kwargs['pk']
        target_author=get_object_or_404(BlogAuthor, pk = id)
        return Post.objects.filter(author=target_author).filter(is_banned=False)
        
    def get_context_data(self, **kwargs):
        """ shtimi i te dhenave te autorit """
        
        context = super(PostListByAuthorView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
        return context
    


class PostDetailView(generic.DetailView):

    model = Post
    
    def get_context_data(self, **kwargs):
        
        context = super(PostDetailView, self).get_context_data(**kwargs)

        post = get_object_or_404(Post, pk = self.kwargs['pk'])
        total_likes = post.total_likes()
        
        liked = False
        if post.like.filter(id=self.request.user.id).exists():
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

    def get_success_url(self): 
        """ kthimi ne url specifike mbas postimit te komentit """
    
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})
   


class PostReportCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
   
    model = PostReport
    fields = ['comment_report',]
    success_url = '/success/'
    success_message = "Your report was created successfully"

    def get_context_data(self,*args, **kwargs):
        """ shtimi i te dhenave te nje posti ne templatin postreport_form.html """
        
        context = super(PostReportCreateView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """ lidhja e autorit me postin qe do raportoje  """
       
        form.instance.author = self.request.user  #vendosja e nje useri si autor i Reportit
        form.instance.blog_report = get_object_or_404(Post, pk = self.kwargs['pk'])  
        return super(PostReportCreateView, self).form_valid(form)

    def get_success_url(self, *args): 
        """ kthimi ne url specifike mbas raportimit  """
        
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})
        


    
    
    



