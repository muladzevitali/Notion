from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class CommentViewSet(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post, pk=kwargs.get("post_pk"))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)

        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs.get("post_pk"))
