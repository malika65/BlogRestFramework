from rest_framework import serializers
from api_ex.models import Tag
from .posts import PostDetailSerializer

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagDetailSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer(many=True)
    class Meta:
        model = Tag
        fields = ('name','post')

    
class TagCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        tag = Tag(**validated_data)
        tag.save()
        return tag

    class Meta:
        model = Tag
        exclude = ('id','post')


