from django.urls import path,include
from . import views
app_name = "blog"

urlpatterns = [
    # path("",views.PostList.as_view(),name="list-post"),
    # path("post/create/", views.PostCreate.as_view(), name="create-post"),
    # path("post/detail/<int:pk>/", views.PostDetail.as_view(), name="detail-post"),
    # path("post/update/<int:pk>/", views.PostUpdate.as_view(), name="update-post"),
    # path("post/delete/<int:pk>/", views.PostDelete.as_view(), name="delete-post"),
    path("api/v1/", include("blog.api.v1.urls"), name="api"),
]
