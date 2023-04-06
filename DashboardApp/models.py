from django.db import models 
from CursoIngles.settings import MEDIA_URL, STATIC_URL 
from datetime import datetime 
from django.forms import model_to_dict 
from django.contrib.auth.models import User 
import random 


class CategoryModel(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)       
        return item    

    class Meta:
        verbose_name ='Category'
        verbose_name_plural = 'Categorys'
        ordering = ['id']


class QuestionModel(models.Model):
    text = models.TextField(verbose_name="Question text") 
    category = models.ForeignKey(CategoryModel, related_name="category", on_delete=models.CASCADE)   
    max_puntaje = models.IntegerField(verbose_name='Maximo Puntaje', default=1) 

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


class PreguntasRespondidas(models.Model):
	quizUser = models.ForeignKey(QuizUser, on_delete=models.CASCADE, related_name='intentos')
	pregunta = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(ChooseQuestionModel, on_delete=models.CASCADE, null=True)
	correcta  = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)
        

LEVEL_CHOICES = (
    ('basic','BASIC'),
    ('intermediate', 'INTERMEDIATE'),
    ('advance','ADVANCE'),)


class CourseModel(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name')  
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)   
    description = models.TextField(verbose_name="Description")    
    level  = models.CharField(max_length=12, choices=LEVEL_CHOICES, default='basic')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)       
        return item    

    class Meta:
        verbose_name ='Course'
        verbose_name_plural = 'Courses'
        ordering = ['id']