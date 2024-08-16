from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    return HttpResponse("Welcome to my Weblog.")


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'posts/post_details.html', context=context)
