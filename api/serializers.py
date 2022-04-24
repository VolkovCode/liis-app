from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Post

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
