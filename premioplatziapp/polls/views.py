# from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))


def detail(request, question_id):
    return HttpResponse(f"Esta viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Esta viendo los resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")