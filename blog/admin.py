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
    search_fields = ('name', 'dept_code')
    ordering = ('dept_code', 'name')


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_filter = ('dept',)
    search_fields = ('title', 'sub_code', 'dept')

