
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render,HttpResponseRedirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.urls import reverse

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by("-publication_date")[:5]

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

#All view
# def index(request):
#     latest_question_list = Question.objects.order_by("-publication_date")[:5]
#     context = {
#         'latest_question_list' : latest_question_list
#     }

#     return render(request, "polls/index.html" ,context)


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
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html',{'question':question})

# #Results view
# def results(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html', {"question":question})
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

#Vote view
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))