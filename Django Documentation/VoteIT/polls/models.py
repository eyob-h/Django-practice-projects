from django.db import models

# Create your models here.

from django.db import models

class Question(models.Model):
    question_text = models.TextField(max_length=200)
    publication_date = models.DateTimeField("date published")


    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    publication_date = models.DateTimeField("date published")
    
    