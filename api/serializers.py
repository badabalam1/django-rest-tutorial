from rest_framework import serializers
from .models import Bucketlist
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = UserSerializer(read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')