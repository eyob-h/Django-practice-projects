from django.http import JsonResponse
from .models import Bucket
from .serializers import BucketSerializer

def getBuckets(request):
    #get buckets
    buckets = Bucket.objects.all()

    #serialize them
    serializer = BucketSerializer(buckets, many=True)
    
    #return json
    # return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'data': serializer.data})