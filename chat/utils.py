# from django.contrib.auth import get_user_model
from django.db.models import Count
from .models import Message
from django.db.models import Count, Case, When, IntegerField
from django.contrib.auth.models import User

def get_users_and_unread_message_count(current_user):
    # User = get_user_model()

    other_users = User.objects.exclude(id=current_user.id)
    return other_users.annotate(
        unread_count=Count(
            Case(
                When(sent_messages__receiver=current_user.id, sent_messages__is_read=False, then='sent_messages'),
                default=None,
                # output_field=IntegerField()
            )
        )
    )
    users_and_unread_message_count = []
    for user in annotated_users:
        users_and_unread_message_count.append({"id":user.id, "username":user.username, "unread_count":user.unread_count})

    return users_and_unread_message_count

def get_users_and_message(sender, receiver):
    messages = Message.objects.filter(
        sender=sender,
        receiver=receiver
    ) | Message.objects.filter(
        sender=receiver,
        receiver=sender
    ).order_by('timestamp')

    return {
        'other_user': receiver,
        'messages': messages,
    }