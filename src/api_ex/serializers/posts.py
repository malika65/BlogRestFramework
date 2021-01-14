from rest_framework import serializers
from api_ex.models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('body','tags',)

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

class PostCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        post = Post(**validated_data)
        post.save()
        if tags:
            for i in tags:
                post.tags.add(i)
        return post

    class Meta:
        model = Post
        exclude = ('id',)
    
class PostDestroySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)