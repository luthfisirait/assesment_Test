from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    body = serializers.CharField()
    author = UserSerializer()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()