from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from ..models import Message
from ..utils import get_users_and_unread_message_count, get_users_and_message

@login_required
def chat_page(request):
    # Retrieve a list of users and their unread message counts
    users_and_unread_count = get_users_and_unread_message_count(request.user)
    context = {
        'users_and_unread_count': users_and_unread_count,
    }
    return render(request, 'chat_page.html', context)

@login_required
def user_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    received_messages = Message.objects.filter(receiver=request.user, sender=other_user)

    # Mark unread received messages as read for the receiver
    unread_received_messages = received_messages.filter(is_read=False)
    unread_received_messages.update(is_read=True)
    
    return render(request, 'user_chat.html', get_users_and_message(request.user,other_user))