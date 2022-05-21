# from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question
    })

def vote(request, question_id):
    # return HttpResponse(f"Estás votando a la pregunta número {question_id}")
    question = get_object_or_404(Question,pk=question_id)
    try:
        # intentando obtener la respuesta del usuario que viene por post del formulario en un diccionario
        # request.POST --> es un objeto similar a un diccionario que le permite acceder a los datos 
        # enviados por nombre del input. En este caso, request.POST['choice'] devuelve el ID de la 
        # opción seleccionada, como una cadena. request.POST los valores son siempre cadenas.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # KeyError: si el usuario no selecciona una respuesta intentamos acceder key que no exite
        # Choice.DoesNotExist: si no existe la respuesta con el id recibido
        # Vuelva a mostrar el formulario de votación de preguntas
        return render(request, 'polls/detail.html', {
            'question': question,
            # 'error_messege': "You didn't select a choice.",
            'error_messege': "No elegiste una respuesta.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # siempre que se trabaja con formularios utilizamos HttpResponseRedirect para redirecionar
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))