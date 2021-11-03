from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="comments"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordering = ("-created_at",)

    def __str__(self):
        return f"{self.post.id} - {self.author} - {self.content}"


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    post_url = models.URLField()
    num_upvote = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=100, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ordering = ("-created_at",)

    def __str__(self):
        return f"{self.author} - {self.title}"
