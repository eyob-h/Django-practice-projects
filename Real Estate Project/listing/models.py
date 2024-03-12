from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    size = models.IntegerField()
    address = models.CharField(max_length=100)
    # owner = models.ForeignKey
    # image

    def __str__(self):
        return self.title