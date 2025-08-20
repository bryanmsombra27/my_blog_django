from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(),
         name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
