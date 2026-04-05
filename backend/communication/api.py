from django.db.models import Prefetch
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response

from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Conversation.objects.filter(members__in=[self.request.user.id])
            .prefetch_related(
                'members',
                'potential_clients',
                'reported_by',
                Prefetch(
                    'messages',
                    queryset=ConversationMessage.objects.select_related('created_by').order_by('-created_at', '-id'),
                    to_attr='prefetched_messages',
                ),
            )
            .distinct()
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        convo = self.get_object()
        latest = convo.messages.order_by('-created_at', '-id').first()
        if latest:
            response.data['latest_message'] = {
                'id': latest.id,
                'content': latest.content,
                'created_at': latest.created_at,
                'created_by': latest.created_by_id,
                'has_attachment': bool(latest.attachment),
            }
        return response

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.members.add(self.request.user)

    def perform_destroy(self, instance):
        if not instance.members.filter(id=self.request.user.id).exists():
            raise PermissionDenied('Not a member of this conversation.')
        instance.delete()

    @action(detail=True, methods=['post'])
    def toggle_potential_client(self, request, pk=None):
        conversation = self.get_object()
        user = request.user
        if conversation.potential_clients.filter(id=user.id).exists():
            conversation.potential_clients.remove(user)
            flagged = False
        else:
            conversation.potential_clients.add(user)
            flagged = True
        return Response({'is_potential_client': flagged})

    @action(detail=True, methods=['post'])
    def report(self, request, pk=None):
        conversation = self.get_object()
        user = request.user
        if conversation.reported_by.filter(id=user.id).exists():
            conversation.reported_by.remove(user)
            reported = False
        else:
            conversation.reported_by.add(user)
            reported = True
        return Response({'is_reported': reported})


class ConversationMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationMessageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_queryset(self):
        return (
            ConversationMessage.objects.filter(conversation__members__in=[self.request.user.id])
            .select_related('conversation', 'created_by')
            .order_by('created_at', 'id')
            .distinct()
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        conversation = serializer.validated_data.get('conversation')
        if not conversation.members.filter(id=self.request.user.id).exists():
            raise PermissionDenied('Not a member of this conversation.')
        serializer.save(created_by=self.request.user)
        Conversation.objects.filter(id=conversation.id).update(modified_at=timezone.now())

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.created_by_id != self.request.user.id:
            raise PermissionDenied('You can only edit your own messages.')
        latest_id = (
            instance.conversation.messages.order_by('-created_at', '-id')
            .values_list('id', flat=True)
            .first()
        )
        if latest_id != instance.id:
            raise PermissionDenied('Only the latest message can be edited.')
        serializer.save(edited_at=timezone.now())
        Conversation.objects.filter(id=instance.conversation_id).update(modified_at=timezone.now())

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        raise PermissionDenied('Messages cannot be deleted.')
