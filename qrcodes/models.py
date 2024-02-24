from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class QRCode(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    code = models.ImageField(upload_to='qrcodes/')


class CheckIn(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='checkins/')
    timestamp = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
