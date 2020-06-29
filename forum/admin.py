from django.contrib import admin
from .models import Forum
# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Forum

admin.site.register(Forum, ForumAdmin)
