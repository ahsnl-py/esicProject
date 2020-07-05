from django.contrib import admin
from .models import (
    Post, 
    Department, 
    Subject, 
    PostImage
)

class PostImageAdmin(admin.StackedInline):
    model = PostImage
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
   
    class Meta:
        model=Post
        

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass



# Register your models here.
"""Subject view in Admin"""
admin.site.register(Subject)

"""Subject view in Admin"""
admin.site.register(Department)


