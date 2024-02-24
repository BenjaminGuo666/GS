from django.db import models
from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()  # 添加日期字段
    start_time = models.TimeField()  # 添加开始时间字段
    end_time = models.TimeField()  # 添加结束时间字段
    location = models.CharField(max_length=255)  # 添加地点字段
    # 其他字段...


# Create your models here.
