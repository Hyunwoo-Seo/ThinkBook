from django.urls import path
from . import views

app_name='board'

urlpatterns = [
    path('create/', views.post_create, name='post_create'),#주소 변경 필요
    path('detail/<int:pk>/', views.postDetailView, name='post_detail'),#주소 변경 필요
    path('list/', views.postListView, name='post_list'),#주소 변경 필요
    path('delete/', views.postDelete, name='postDelete'),#주소 변경 필요
    path('comment_delete/', views.commentDelete, name='commentDelete'),#주소 변경 필요
    path('comment/', views.comment, name='comment')#주소 변경 필요
]