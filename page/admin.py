from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    list_filter = ("title",)
    search_fields = ['title', 'content']

    
    
 
    


admin.site.register(Post, PostAdmin)