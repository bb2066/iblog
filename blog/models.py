from django.db import models
from django.contrib import admin
from django.utils.html import format_html
# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    images = models.ImageField(upload_to='category/')
    title = models.CharField(max_length=100)
    url= models.CharField(max_length=50, default="")
    add_date = models.DateTimeField(auto_now_add=True , null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:55px; height:50px; border-radius:50%"/>'.format(self.images))
    
    def __str__(self):
        return self.title
    


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description=models.TextField(default="")    
    content = models.TextField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True , null=True)

   
    

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:55px; height:50px; border-radius:50%"/>'.format(self.images))
    
    def __str__(self):
        return self.title