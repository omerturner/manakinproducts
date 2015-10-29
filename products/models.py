from django.db import models


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.TextField()
    amz_link = models.URLField(max_length=255)
    order = models.IntegerField(default=999)
    image = models.ImageField(upload_to='', default='./no_image.png')
    image2 = models.ImageField(upload_to='', default='./no_image.png')
    image3 = models.ImageField(upload_to='', default='./no_image.png')
    image4 = models.ImageField(upload_to='', default='./no_image.png')
    image5 = models.ImageField(upload_to='', default='./no_image.png')
    image6 = models.ImageField(upload_to='', default='./no_image.png')

    def __str__(self):
        return self.title
