from django.db import models

class SEO(models.Model):
    attr = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name