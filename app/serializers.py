from rest_framework import serializers
from django.db.models import Count

from .models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.username', read_only=True)
    likes = serializers.IntegerField(source='like.count')

    class Meta:
        model = Post
        fields = ['id','body', 'author', 'likes']
