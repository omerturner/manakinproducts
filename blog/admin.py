from django.contrib import admin

from .models import Post, Publisher

class PostInline(admin.StackedInline):
    model = Post    

    
class PublisherAdmin(admin.ModelAdmin):
    inlines = [PostInline,]

    
admin.site.register(Publisher, PublisherAdmin)   
admin.site.register(Post)