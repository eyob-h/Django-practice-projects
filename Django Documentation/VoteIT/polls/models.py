import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

from django.db import models

class Question(models.Model):
    question_text = models.TextField(max_length=200)
    publication_date = models.DateTimeField("date published")

    @admin.display(
        boolean=True,
        ordering="publication_date",
        description="Published Recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now

    # def was_published_recently(self):
    #     return self.publication_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    

    def __str__(self):
        return self.choice_text
    
    