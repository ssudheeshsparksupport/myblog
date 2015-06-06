from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'photo', 'content', 'public']



admin.site.register(Post, PostAdmin)
