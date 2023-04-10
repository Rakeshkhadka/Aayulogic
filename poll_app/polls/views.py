from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Questions
from django.template import loader

# Create your views here.
def main(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # output = ", ".join([q.question_text for q in latest_question_list])
    context = {
        "latest_question_list": latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

