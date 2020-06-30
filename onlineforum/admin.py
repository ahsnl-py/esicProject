from django.contrib import admin
from .models import ChatForum
# Register your models here.


class ChatForumAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = ChatForum

admin.site.register(ChatForum)