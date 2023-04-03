from django.db import models 
from CursoIngles.settings import MEDIA_URL, STATIC_URL 
from datetime import datetime 
from django.forms import model_to_dict 
from django.contrib.auth.models import User 
import random 



class QuestionModel(models.Model):
    text = models.TextField(verbose_name="Question text") 
    max_puntaje = models.IntegerField(verbose_name='Maximo Puntaje', default=3) 

    def __str__(self): 
        return self.text 
    
    def toJSON(self): 
        item = model_to_dict(self) 
        return item 

class ChooseQuestionModel(models.Model): 
    MAXIMUN_RESPONSE = 4 
    question = models.ForeignKey(QuestionModel, related_name="questions", on_delete=models.CASCADE)  
    correct = models.BooleanField(verbose_name="is the right question", default=False, null=False) 
    text = models.TextField(verbose_name="Answer text")

    def __str__(self): 
        return self.text 
    
    def toJSON(self): 
        item = model_to_dict(self) 
        item['question'] = self.question.toJSON() 
        return item 
  
    
class QuizUser(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

	def crear_intentos(self, pregunta):
		intento = PreguntasRespondidas(pregunta=pregunta, quizUser=self)
		intento.save()

	def obtener_nuevas_preguntas(self):
		respondidas = PreguntasRespondidas.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
		preguntas_restantes = QuestionModel.objects.all()
		 
		return random.choice(preguntas_restantes)


	def validar_intento(self, pregunta_respondida, respuesta_selecionada):
		if pregunta_respondida.pregunta_id != respuesta_selecionada.question_id:
			return

		pregunta_respondida.respuesta_selecionada = respuesta_selecionada
		if respuesta_selecionada.correct is True:
			pregunta_respondida.correct = True
			pregunta_respondida.puntaje_obtenido = respuesta_selecionada.question.max_puntaje
			pregunta_respondida.respuesta = respuesta_selecionada

		else:
			pregunta_respondida.respuesta = respuesta_selecionada

		pregunta_respondida.save()

		self.actualizar_puntaje()

	def actualizar_puntaje(self):
		puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(
			models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

		self.puntaje_total = puntaje_actualizado
		self.save()

class PreguntasRespondidas(models.Model):
	quizUser = models.ForeignKey(QuizUser, on_delete=models.CASCADE, related_name='intentos')
	pregunta = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(ChooseQuestionModel, on_delete=models.CASCADE, null=True)
	correcta  = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)