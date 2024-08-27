from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializers

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

# class PostListView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PostDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serialized_posts = PostSerializers(posts, many=True)
#         return Response(serialized_posts.data)
#
#     def post(self, request):
#         serialized_data = PostSerializers(data=request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response(serialized_data.data, status=status.HTTP_201_CREATED)
#         return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetailView(APIView):
#
#     def get_object(self, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Exception as E:
#             raise Http404
#         return post
#
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serialized_post = PostSerializers(post)
#         return Response(serialized_post.data)
#
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serialized_post = PostSerializers(post, data=post)
#         if serialized_post.is_valid():
#             serialized_post.save()
#             return Response(serialized_post.data, status=status.HTTP_200_OK)
#         return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
