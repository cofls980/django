from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Text(models.Model):
    pid = models.IntegerField(default=0)
    ptext = models.CharField(max_length=20)
    pid.primary_key = True

    def __str__(self):
        return self.ptext


class Color(models.Model):
    pid = models.IntegerField(default=0)
    pcolor = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published', default=0)
    pid.primary_key = True

    def __str__(self):
        return self.pcolor

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)