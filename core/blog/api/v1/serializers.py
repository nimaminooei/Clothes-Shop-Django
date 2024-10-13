from rest_framework import serializers
from blog.models import Post,Like,Comment
from django.utils.timesince import timesince
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'author']

class PostSerializer(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    humanized_published_date = serializers.SerializerMethodField()
    user_like = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'author', 'category', 'tag', 'title', 'content', 'status', 'like_count','comment_count','humanized_published_date','user_like']
        read_only_fields = ["author"]
    
    def get_humanized_published_date(self, obj):
        return timesince(obj.updated_date) + " ago"
    
    def to_representation(self, obj):
        ret = super(PostSerializer, self).to_representation(obj)
        ret.pop("author", None)
        return ret
    
    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_user_like(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return obj.likes.filter(author=user).exists()
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)  

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at', 'replies', 'parent']  
        read_only_fields = ['id', 'author', 'created_at', 'replies']

    def create(self, validated_data):
        request = self.context.get('request')
        return Comment.objects.create(author=request.user, **validated_data)
