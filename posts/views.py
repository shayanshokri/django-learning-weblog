from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Comment
from .forms import PostForm
from django.views import generic

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def home(request):
    print(request.data)
    return Response(dict(request.data), status=status.HTTP_400_BAD_REQUEST)


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)


def post_details(request, pk):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound(' Post not found!')
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'posts/post_details.html', context=context)


class PostDetails(generic.DetailView):
    model = Post
    template_name = 'posts/post_details.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetails, self).get_context_data()
        context['comments'] = Comment.objects.filter(post=kwargs['object'].pk)
        return context


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts')
    else:
        form = PostForm()
        return render(request, 'posts/post_create.html', {'form': form})


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
