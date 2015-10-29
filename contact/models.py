from django.db import models

# Create your models here.
class WebsiteContact(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject