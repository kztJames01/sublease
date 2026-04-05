from rest_framework import serializers

from .models import Conversation, ConversationMessage


class ConversationSerializer(serializers.ModelSerializer):
    members_detail = serializers.SerializerMethodField()
    other_member = serializers.SerializerMethodField()
    latest_message = serializers.SerializerMethodField()
    is_potential_client = serializers.SerializerMethodField()
    is_reported = serializers.SerializerMethodField()

    def _user_payload(self, user):
        full_name = f'{user.first_name} {user.last_name}'.strip() or user.username
        initials = ''.join(part[0] for part in full_name.split()[:2]).upper() or user.username[:2].upper()
        return {
            'id': user.id,
            'username': user.username,
            'display_name': full_name,
            'initials': initials,
            'email': user.email,
        }

    def get_members_detail(self, obj):
        return [self._user_payload(user) for user in obj.members.all()]

    def get_other_member(self, obj):
        request = self.context.get('request')
        current_user_id = getattr(getattr(request, 'user', None), 'id', None)
        other = next((user for user in obj.members.all() if user.id != current_user_id), None)
        return self._user_payload(other) if other else None

    def get_latest_message(self, obj):
        prefetched = getattr(obj, 'prefetched_messages', None)
        latest = prefetched[0] if prefetched else obj.messages.order_by('-created_at', '-id').first()
        if not latest:
            return None
        return {
            'id': latest.id,
            'content': latest.content,
            'created_at': latest.created_at,
            'created_by': latest.created_by_id,
            'has_attachment': bool(latest.attachment),
        }

    def get_is_potential_client(self, obj):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        return bool(user and user.is_authenticated and obj.potential_clients.filter(id=user.id).exists())

    def get_is_reported(self, obj):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        return bool(user and user.is_authenticated and obj.reported_by.filter(id=user.id).exists())

    class Meta:
        model = Conversation
        fields = (
            'id',
            'item',
            'members',
            'members_detail',
            'other_member',
            'latest_message',
            'is_potential_client',
            'is_reported',
            'created_at',
            'modified_at',
        )
        read_only_fields = ('created_at', 'modified_at')


class ConversationMessageSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    attachment_url = serializers.SerializerMethodField()
    attachment_name = serializers.SerializerMethodField()
    attachment_kind = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()

    def get_author(self, obj):
        full_name = f'{obj.created_by.first_name} {obj.created_by.last_name}'.strip() or obj.created_by.username
        initials = ''.join(part[0] for part in full_name.split()[:2]).upper() or obj.created_by.username[:2].upper()
        return {
            'id': obj.created_by.id,
            'display_name': full_name,
            'initials': initials,
        }

    def get_attachment_url(self, obj):
        if not obj.attachment:
            return None
        request = self.context.get('request')
        url = obj.attachment.url
        return request.build_absolute_uri(url) if request else url

    def get_attachment_name(self, obj):
        return obj.attachment.name.split('/')[-1] if obj.attachment else None

    def get_attachment_kind(self, obj):
        if not obj.attachment:
            return None
        name = obj.attachment.name.lower()
        if any(name.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
            return 'image'
        if any(name.endswith(ext) for ext in ['.mp4', '.mov', '.avi', '.webm', '.mkv']):
            return 'video'
        return 'file'

    def get_can_edit(self, obj):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        if not user or not user.is_authenticated or obj.created_by_id != user.id:
            return False
        latest_id = (
            obj.conversation.messages.order_by('-created_at', '-id')
            .values_list('id', flat=True)
            .first()
        )
        return latest_id == obj.id

    def validate(self, attrs):
        instance = getattr(self, 'instance', None)
        content = attrs.get('content', getattr(instance, 'content', ''))
        attachment = attrs.get('attachment', getattr(instance, 'attachment', None))
        if not str(content).strip() and not attachment:
            raise serializers.ValidationError('Message content or an attachment is required.')
        return attrs

    class Meta:
        model = ConversationMessage
        fields = (
            'id',
            'conversation',
            'content',
            'attachment',
            'attachment_url',
            'attachment_name',
            'attachment_kind',
            'created_at',
            'edited_at',
            'created_by',
            'author',
            'can_edit',
        )
        read_only_fields = ('created_at', 'edited_at', 'created_by')
