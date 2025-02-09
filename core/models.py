from django.db import models

class Booking(models.Model):
    SESSION_TYPE_CHOICES = [
        ('2-station', '2 Station'),
        ('4-station', '4 Station'),
    ]

    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    session_type = models.CharField(max_length=10, choices=SESSION_TYPE_CHOICES)
    payment_id = models.CharField(max_length=255)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - {self.session_type} on {self.date} at {self.time}"
