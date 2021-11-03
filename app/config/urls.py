from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("check_health/", views.check_health, "check_health"),
    path("api/v1/", include("apps.posts.urls")),
]
