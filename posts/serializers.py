from rest_framework import serializers
from .models import Post


def validate_title(value):
    if len(value) < 5:
        raise serializers.ValidationError("O título deve ter pelo menos 5 caracteres.")
    return value


def validate_content(value):
    if len(value) < 5:
        raise serializers.ValidationError("O conteúdo deve ter pelo menos 20 caracteres.")
    return value


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'created_datetime']

