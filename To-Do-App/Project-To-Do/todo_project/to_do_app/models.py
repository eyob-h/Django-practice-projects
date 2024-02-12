from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # due_date = models.DateTimeField(editable=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title