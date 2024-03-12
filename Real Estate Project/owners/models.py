from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    # properties = models.ForeignKey()