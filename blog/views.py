from django.shortcuts import render
from .models import Post


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"latest_posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html", context={"slug": slug})
