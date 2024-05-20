from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Profile, SavedPost
from review.models import Favorite

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image',]

class SavedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['author', 'image']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    saved_posts = SavedPostSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'is_active', 'profile', 'saved_posts']
