from rest_framework import serializers
from .models import Bucket

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ['id', 'name', 'points', 'description']

    # name = models.CharField(max_length=200)
    # points = models.IntegerField()
    # description = models.CharField(max_length=500)