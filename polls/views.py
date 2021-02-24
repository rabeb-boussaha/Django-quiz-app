from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    context = {}
    return render(request,'polls/home.html',contexe)

def create(request):
    context = {}
    return render(request,'polls/create.html',contexe)

def vote(request, polls_id):
    context = {}
    return render(request,'polls/vote.html',contexe)

def results(request, polls_id):
    context = {}
    return render(request,'polls/results.html',contexe)

