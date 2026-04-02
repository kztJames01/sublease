from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(members__in=[self.request.user.id]).distinct()

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.members.add(self.request.user)


class ConversationMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ConversationMessage.objects.filter(
            conversation__members__in=[self.request.user.id]
        ).distinct()

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get('conversation')
        if not conversation.members.filter(id=self.request.user.id).exists():
            raise PermissionDenied('Not a member of this conversation.')
        serializer.save(created_by=self.request.user)
