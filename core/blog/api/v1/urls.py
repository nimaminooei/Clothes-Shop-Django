from django.urls import path

from .views import ApiPostView, ApiPostDetail,AddLikeAPIView,CommentListCreateAPIView,CommentRetrieveUpdateDestroyAPIView

app_name = "api"

urlpatterns = [
    path("posts/", ApiPostView.as_view(), name="post_list"),
    path(
        "post-detail/<int:id>/",
        ApiPostDetail.as_view(),
        name="post_detail",
    ),
    # Like Api
    path('post/like/<int:post_id>/', AddLikeAPIView.as_view(), name='like-opt'),
    # Coomments Api 
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),

]
