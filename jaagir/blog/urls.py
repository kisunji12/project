from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostApplyView


urlpatterns = [
        path('', PostListView.as_view(), name='blog-home'),
        path('detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
        path('detail/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
        path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
        path('create/', PostCreateView.as_view(), name='post-create'),
        path('apply/', PostApplyView.as_view(), name='post-apply'),
]
