from django.shortcuts import render

from app.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts":posts})
