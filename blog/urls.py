from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('newpost/', views.NewPost, name='newpost'),
    path('post/<int:pk>', views.PostDetail, name='postDetail'),
    path('updatePost/<int:pk>/', views.UpdatePost, name="updatePost"),
    path('deletePost/<int:pk>/', views.DeletePost, name="deletePost"),


]