from django.conf import settings
from rest_framework import serializers

from .models import ChatForum

MAX_POST_LENGTH = settings.MAX_POST_LENGTH
#FORUM_ACTION_OPTIONS = settings.FORUM_ACTION_OPTIONS

class ChatForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatForum
        fields = ['content']

    def validate_content(self, value):
            if len(value) > MAX_POST_LENGTH:
                raise serializers.ValidationError("This forum is too long")
            return value