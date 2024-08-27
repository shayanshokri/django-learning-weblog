from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializers


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializers(posts, many=True)
        return Response(serialized_posts.data)

    def post(self, request):
        serialized_data = PostSerializers(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):

    def get_object(self, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Exception as E:
            raise Http404
        return post

    def get(self, request, pk):
        post = self.get_object(pk)
        serialized_post = PostSerializers(post)
        return Response(serialized_post.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serialized_post = PostSerializers(post, data=post)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data, status=status.HTTP_200_OK)
        return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

