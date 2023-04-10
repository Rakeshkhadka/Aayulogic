from django.db import models

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("publication date")


class Choices(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)
