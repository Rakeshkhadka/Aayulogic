from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("publication date")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choices(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)

