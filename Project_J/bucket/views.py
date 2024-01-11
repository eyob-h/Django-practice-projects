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
    

@api_view(['GET','PUT','UPDATE'])
def singleBucket(request, id):
    
    #check the validity of the request
    try:
        bucket = Bucket.objects.get(pk=id)
    except Bucket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = BucketSerializer(bucket)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = BucketSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)