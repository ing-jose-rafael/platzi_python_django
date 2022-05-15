from django.db import models

# Create your models here.
# modelo de preguntas
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

# modelo de la respuesta
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE) # si elinimo la pregunta se elimina la respuestas
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0) # cuantos votos tiene cada resp, será un contador

