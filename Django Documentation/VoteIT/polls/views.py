from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question, Choice
from django.http import Http404

#All view
def index(request):
    latest_question_list = Question.objects.order_by("-publication_date")[:5]
    context = {
        'latest_question_list' : latest_question_list
    }

    return render(request, "polls/index.html" ,context)


#Detail View
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist.")
#     return render(request, 'polls/detail.html', {"question":question})

#Using a shortcut for the try except method
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

#Results view
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)