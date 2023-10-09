from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from ..models import Message
from ..utils import get_users_and_message

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request, receiver_id):
    # todo clear context on submit
    # todo ceck why chat messages are not getting marked as read
    sender = request.user
    content = request.data.get('message')  # Assuming the message content is sent as 'message' in the POST data

    Message.objects.create(sender=sender, receiver_id=receiver_id, content=content) 
    
    other_user = get_object_or_404(User, id=receiver_id)
    return render(request, 'user_chat.html', get_users_and_message(sender, other_user))