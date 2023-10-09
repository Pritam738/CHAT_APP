# chat/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User  # Import the User model
from .models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Include user-related fields as needed

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()  # Nested serializer for sender
    receiver = UserSerializer()  # Nested serializer for receiver

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'content', 'timestamp', 'is_read')
