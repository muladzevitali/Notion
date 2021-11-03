from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            "id",
            "title",
            "post_url",
            "url",
            "num_upvote",
            "author",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "num_upvote", "created_at", "updated_at")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ("id", "author", "content", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")
