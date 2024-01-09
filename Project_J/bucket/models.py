from django.db import models

class Bucket(models.Model):
    name = models.CharField(max_length=200)
    points = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} bucket {self.points}"