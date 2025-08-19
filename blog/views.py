from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post-detail.html", {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        return render(request, "blog/post-detail.html", {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
        })
