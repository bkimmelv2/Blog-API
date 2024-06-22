from .models import Blog
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Blog Serializer
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model to be serialized
        model = Blog
        # output fields
        fields = ['id', 'title', 'body']