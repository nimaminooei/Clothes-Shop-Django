from rest_framework.response import Response
from blog.models import Post,Like,Comment
from .serializers import PostSerializer,CommentSerializer
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from django.shortcuts import get_object_or_404


class ApiPostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(status=True)
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ApiPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_object(self, queryset=None):
        obj = get_object_or_404(Post, pk=self.kwargs["id"])

        return obj

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return Response(
            {"detail": "successfully removed"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class AddLikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=int(post_id))
        user = request.user
        like, created = Like.objects.get_or_create(post=post, author=user)
        if created:
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Post already liked"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, post_id):
        
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        
        like = Like.objects.get(post=post, author=user)
        
        if like:
            like.delete()
            return Response({"message": "Like removed"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Like not found"}, status=status.HTTP_400_BAD_REQUEST)
        
class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post=post, parent=None) 

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        parent_id = self.request.data.get('parent')
        parent = None
        if parent_id:
            parent = get_object_or_404(Comment, id=parent_id)
        serializer.save(author=self.request.user, post=post, parent=parent)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)