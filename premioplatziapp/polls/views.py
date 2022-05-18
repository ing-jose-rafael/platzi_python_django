from django.shortcuts import render, get_object_or_404
# from django.template import loader

from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = Question.objects.all()
    # template = loader.get_template('polls/index.html') # Opcion 1
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context,request)) # Opcion 1
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # return HttpResponse(f"Esta viendo la pregunta número {question_id}")
    context = {
        'question': question,
    }
    return render(request,'polls/detail.html',context)

def results(request, question_id):
    return HttpResponse(f"Esta viendo los resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")