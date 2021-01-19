from django.contrib import admin

# Register your models here.
from .models import Post, BlogAuthor, Comment, PostReport


admin.site.register(Post)
admin.site.register(BlogAuthor)
admin.site.register(Comment)
admin.site.register(PostReport)

class PostCommentsInline(admin.TabularInline):
    """ shfaqja e komenteve inline ne nje post """
    model = Comment
    max_num=0



