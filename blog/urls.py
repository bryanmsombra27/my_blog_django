from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post, name="post-detail-page"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
