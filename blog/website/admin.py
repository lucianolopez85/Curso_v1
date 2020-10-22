from django.contrib import admin 
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','sub_title','full_name')
    search_fields = ('title','sub_title')

admin.site.register(Post, PostAdmin) 
