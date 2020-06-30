from django.conf import settings
from rest_framework import serializers

from .models import ChatForum

MAX_POST_LENGTH = settings.MAX_POST_LENGTH
FORUM_ACTION_OPTIONS = settings.FORUM_ACTION_OPTIONS

class ChatForumActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip() 
        if not value in FORUM_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for forums")
        return value

class ChatForumSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = ChatForum
        fields = ['id', 'content', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()
        
    def validate_content(self, value):
            if len(value) > MAX_POST_LENGTH:
                raise serializers.ValidationError("This forum is too long")
            return value