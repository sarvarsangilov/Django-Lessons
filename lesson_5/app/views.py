from django.shortcuts import get_object_or_404, render

from app.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts":posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    return render(request, 'detail.html', {'post': post})
