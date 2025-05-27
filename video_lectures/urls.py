from django.urls import path
from .views import video_lecture_list

urlpatterns = [
    path('video-lectures/', video_lecture_list, name='video_lecture_list'),
]
