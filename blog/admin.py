from django.contrib import admin
from .models import (
    Post, 
    Department, 
    Subject, 
    #PostImage,
    PostFile
)

class PostFileInline(admin.TabularInline):
    model = PostFile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    inlines = [
        PostFileInline,
    ]
   
    class Meta:
        model=Post
        

admin.site.register(PostFile)

# Register your models here.
"""Subject view in Admin"""
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_filter = ('department_name', )
    ordering = ('department_name', )
    prepopulated_fields = {'subject_slug': ('subject_name',)}
    

"""Subject view in Admin"""
admin.site.register(Department)


