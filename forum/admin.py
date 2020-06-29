from django.contrib import admin
from .models import Forum, ForumLike
# Register your models here.

class ForumLikeAdmin(admin.TabularInline):
        model = ForumLike

class ForumAdmin(admin.ModelAdmin):
    inlines = [ForumLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Forum

admin.site.register(Forum, ForumAdmin)
