from django.db import models


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.TextField()    
    features = models.TextField()
    size = models.CharField(max_length=25, blank=True)
    color = models.CharField(max_length=25, blank=True)
    price = models.FloatField(default=999.9)
    sale_price = models.FloatField(default=999.9)
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
