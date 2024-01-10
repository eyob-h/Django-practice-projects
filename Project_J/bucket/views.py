from django.http import JsonResponse
from .models import Bucket
from .serializers import BucketSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# @api_view('GET','POST','PUT','DELETE')
@api_view(['GET','POST'])
def getBuckets(request):
    
    if request.method == 'GET':
        #get buckets    
        buckets = Bucket.objects.all()

        #serialize them
        serializer = BucketSerializer(buckets, many=True)
        
        #return json
        # return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'data': serializer.data})
    
    if request.method == 'POST':
        serializer = BucketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        