from django.shortcuts import render
from django.shortcuts import get_object_or_404
# from django.http import Http404 no longer needed
from django.http import HttpResponse

from .models import Employee
# Create your views here.

def employee_detail(request, pk):
    
    #There's a better way
    # try:
    #     detail = Employee.objects.get(pk=pk)
    #     context = {
    #         'detail':detail
    #     }
    #     print(context)
    # except:
    #     raise Http404

    detail = get_object_or_404(Employee, pk=pk)
    context = {
        'employee':detail, 
    }
    # return render('home', detail)
    # return HttpResponse(detail)
    return render(request, 'employee_details.html', context)
    