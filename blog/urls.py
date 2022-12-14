from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='blog_detail'),
    path('create/', views.PostCreateView.as_view(), name='blog_create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog_delete'),
    # comment
    path('comment/add/<int:blog_id>/', views.CommentCreateView.as_view(), name='comment_create')
]
