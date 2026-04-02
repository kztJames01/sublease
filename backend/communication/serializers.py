from rest_framework import serializers

from .models import Conversation, ConversationMessage


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ('id', 'item', 'members', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')


class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = ('id', 'conversation', 'content', 'created_at', 'created_by')
        read_only_fields = ('created_at', 'created_by')
