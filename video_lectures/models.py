from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class VideoLecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.URLField(max_length=255, help_text="YouTube video URL")
    thumbnail = models.ImageField(upload_to='video_lectures/thumbnails/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos', null=True, blank=True)

    def __str__(self):
        return self.title
