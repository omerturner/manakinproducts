from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=25, unique=True)
    profile_pic = models.ImageField(upload_to='', default='./no_image.png')
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    post_pic = models.ImageField(upload_to='', default='./no_image.png')
    publisher = models.ForeignKey(Publisher)
    
    def __str__(self):
        return self.title