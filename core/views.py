from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm

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
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.post = post
            new_comment.save()
            form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'core/detail.html', context)
