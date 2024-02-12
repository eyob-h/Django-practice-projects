from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#views in django= Request handlers
#req->res

#Say hi
# def sayHi(request):
#     return HttpResponse("Hi")

#say hi from template
def sayHi(request):
    # return render(request, 'hi.html', {'name': 'Mr. X'})
    return render(request, 'hi.html')