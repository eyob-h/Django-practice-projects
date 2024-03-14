from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    size = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()
    date_listed = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey

    def __str__(self):
        return self.title

class Status(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rented_by = models.CharField(max_length=50)
    
    def __str__(self):
        return self.rented_by