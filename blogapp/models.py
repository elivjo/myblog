from django.db import models

# Create your models here.
from datetime import date
from django.contrib.auth.models import User

class BlogAuthor(models.Model):
    """ info reth nje blogeri """
    author = models.OneToOneField(User, on_delete = models.SET_NULL, null = True) # e njejte si foreignkey por mer nje vlere unike dhe te lidh me modelin User te krijuar nga django
    bio_details = models.TextField(max_length= 500, help_text = "enter your bio details")
    
    class Meta:
        ordering= ["author"]
    
    def __str__(self):
        return self.author.username

class Post(models.Model):
    """ permbajtja e nje posti ne blog """
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=1000, help_text = "Enter your content here")
    post_date = models.DateField(default=date.today)

    class Meta: 
        """ Renditja nga postimi nga me i hershem"""
       
        ordering = ["-post_date"]
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    """ modeli i komenteve ne nje post """

    comment = models.TextField(max_length=1000, help_text="Enter comment about post here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True) #nje koment ka vetem nje autor, nje autor mund te kete shume komente
    post_date= models.DateTimeField(auto_now_add = True)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering=["post_date"]

    def __str__(self):
        return self.comment[:75] + '...'
    



