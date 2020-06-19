from django.contrib import admin
from .models import Post, Department, Courses


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Department)
class DeparmentAdmin(admin.ModelAdmin):
    list_filter = ('name', 'number')
    search_fields = ('name', 'number')


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_filter = ('title', 'code')
    search_fields = ('title', 'code')
