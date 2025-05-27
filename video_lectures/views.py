from django.shortcuts import render
from .models import VideoLecture

def video_lecture_list(request):
    videos = VideoLecture.objects.all()
    return render(request, 'video_lectures/video_lecture_list.html', {'videos': videos})
