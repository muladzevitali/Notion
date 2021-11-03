from django.urls import path
from rest_framework_nested import routers

from . import viewsets, views

posts_router = routers.DefaultRouter(trailing_slash=False)
posts_router.register("posts", viewsets.PostViewSet)

comments_router = routers.NestedSimpleRouter(posts_router, r"posts", lookup="post")
comments_router.register(r"comments", viewsets.CommentViewSet, basename="post-comments")

urlpatterns = posts_router.urls + comments_router.urls
urlpatterns += [
    path("posts/<post_id>/upvote", views.UpVoteApiView.as_view(), name="upvote")
]
