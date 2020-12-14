from django.contrib import admin

# Register your models here.
from .models import Post, BlogAuthor, Comment


admin.site.register(Post)
admin.site.register(BlogAuthor)
admin.site.register(Comment)

class PostCommentsInline(admin.TabularInline):
    """ shfaqja e komenteve inline ne nje post """
    model = Comment
    max_num=0


