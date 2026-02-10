# Сделать доступ к posts/<int:post_id>/comments/


from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)


comment_list_create = CommentViewSet.as_view({
    "get": "list",
    "post": "create",
})

comment_detail = CommentViewSet.as_view({
    "get": "retrieve",
    "patch": "partial_update",
    "put": "update",
    "delete": "destroy",
})

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path("posts/<int:post_id>/comments/", comment_list_create),
    path("posts/<int:post_id>/comments/<int:pk>/", comment_detail),
    path('', include(router.urls))
]
