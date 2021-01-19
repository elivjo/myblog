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
    image = models.ImageField(null= True, blank= True, upload_to = "images/") # imazhet ruhen ne direktorine media/images kur ngarkohen nga perodruesi 
    likes = models.ManyToManyField(User, related_name="blog_post")
    
    class Meta: 
        """ Renditja nga postimi nga me i hershem"""
       
        ordering = ["-post_date"]
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    """ modeli i komenteve ne nje post """

    comment = models.TextField(max_length=1000, help_text="Enter comment about post here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True) #nje koment ka vetem nje autor, nje autor mund te kete shume komente
    post_date= models.DateTimeField(auto_now_add = True)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, null= True)

    class Meta:
        ordering=["-post_date"]

    def __str__(self):

        len_title=30
        if len(self.comment)>len_title:
            titlestring=self.comment[:len_title] + '...'
        else:
            titlestring=self.comment
        return titlestring
    
class PostReport(models.Model):
    """ modeli i reporteve ne nje post """
    
    comment_report = models.TextField(max_length=1000, help_text="Enter comment about post here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True) #nje koment ka vetem nje autor, nje autor mund te kete shume komente
    report_date= models.DateTimeField(auto_now_add = True)
    blog_report = models.ForeignKey(Post, on_delete=models.CASCADE, null= True)

    class Meta:
        ordering=["-report_date"]

    def __str__(self):
        return  self.author.username + " - " + self.comment_report[:10] + " " + "..."


