from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, models


class UpVoteApiView(APIView):
    serializer_class = serializers.PostSerializer

    def get(self, request, post_id):
        post = get_object_or_404(models.Post, pk=post_id)
        post.num_upvote += 1
        post.save()

        return Response(status=status.HTTP_201_CREATED)
