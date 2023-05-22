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

  

class VocavularyModel(models.Model):    
    name = models.CharField(max_length=50,verbose_name='Name')

    def __str__(self): 
        return self.name 
    
    def toJSON(self): 
        item = model_to_dict(self) 
        return item 
  

class DetVocavularyModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)   
    vocavulary = models.ForeignKey(VocavularyModel,on_delete=models.CASCADE)    

    def __str__(self): 
        return self.category.name
    
    def toJSON(self): 
        item = model_to_dict(self) 
        return item 
 
 
class ColVocavularyModel(models.Model):
    vocavulary = models.ForeignKey(VocavularyModel,on_delete=models.CASCADE)    
    name = models.CharField(max_length=50,verbose_name='Name')
    text = models.CharField(max_length=50,verbose_name='Text')

    def __str__(self): 
        return self.name 
    
    def toJSON(self): 
        item = model_to_dict(self) 
        return item 
 
 