from django.contrib import admin 
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','name','categories')   # 'full_name'
    search_fields = ('title','name')

admin.site.register(Post, PostAdmin) 
