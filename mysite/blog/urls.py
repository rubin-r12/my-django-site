from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000
    path('', views.post_list, name='post_list'),
    # 127.0.0.1:8000/post/1
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 127.0.0.1:8000/post/new
    path('post/new/', views.post_new, name='post_new'),
    # 127.0.0.1:8000/post/1/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 127.0.0.1:8000/post/1/delete
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    # 127.0.0.1:8000/drafts
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # 127.0.0.1:8000/post/1/publish
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # 127.0.0.1:8000/post/1/comment
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # 127.0.0.1:8000/comment/1/remove
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # 127.0.0.1:8000/comment/1/approve
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
]