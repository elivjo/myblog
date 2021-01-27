from django.contrib import admin

# Register your models here.
from .models import Post, BlogAuthor, Comment, PostReport



admin.site.register(BlogAuthor)
admin.site.register(Comment)
admin.site.register(PostReport)

class PostAdminSite(admin.ModelAdmin):
    model = Post 
    fields = [ 'title','author','content','post_date', 'image', 'is_banned' ]
    list_display = ('title', 'is_banned')
    actions = ['ban_post']
    
    def ban_post(self, request,queryset, **kwargs):
        queryset.update(is_banned = True)
       
            


admin.site.register(Post, PostAdminSite)


