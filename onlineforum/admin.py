from django.contrib import admin
from .models import ChatForum, ChatForumLike
# Register your models here.

class ChatForumLikeAdmin(admin.TabularInline):
        model = ChatForumLike

class ChatForumAdmin(admin.ModelAdmin):
    inline = [ChatForumLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = ChatForum

admin.site.register(ChatForum)