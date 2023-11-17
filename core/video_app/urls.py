from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('<int:pk>/', views.video_detail, name="video_detail"),
    path('stream/<int:pk>/', views.get_streaming_video, name="stream"),
]