import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# modelo de preguntas
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published",auto_now=True)

    def __str__(self) -> str:
        return self.question_text

    # Metodo que retorna si una publicación es reciente o no,
    # verifica que la pub_date este por delante de ayer a las misma hora del tiempo actual
    # timedelta(days=1) objeto que retorna una diferencia de tiempo
    def was_published_recently(self):
        # timezone.now() - datetime.timedelta(days=1) para restar al tiempo actual un dia, nos vamos hacia atras en el tiempo
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# modelo de la respuesta
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE) # si elinimo la pregunta se elimina la respuestas
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0) # cuantos votos tiene cada resp, será un contador

    def __str__(self) -> str:
        return self.choice_text
