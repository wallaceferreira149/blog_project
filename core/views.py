from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'core/index.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, 'core/detail.html', context)
