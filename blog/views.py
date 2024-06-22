from django.shortcuts import render
from .models import Blog
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    # Main Index query
    queryset = Blog.objects.all()
    # Serialized output
    serializer_class = BlogSerializer
    # optional permissions
    permission_classes = [permissions.AllowAny]
