from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment


def home(request):
    return HttpResponse("Welcome to my Weblog.")


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'posts/post_details.html', context=context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts')
    else:
        form = PostForm()
        return render(request, 'posts/post_create.html', {'form': form})
