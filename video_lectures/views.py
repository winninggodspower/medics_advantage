from django.shortcuts import render
from .models import Course, VideoLecture

def video_lecture_list(request):
    courses = Course.objects.prefetch_related('videos').all()
    videos = VideoLecture.objects.all()
    context = {
        'courses': courses,
        'videos': videos,
    }
    return render(request, 'video_lectures/video_lecture_list.html', context)
