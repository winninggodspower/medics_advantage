from django.db import models

class VideoLecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='video_lectures/')
    thumbnail = models.ImageField(upload_to='video_lectures/thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title
