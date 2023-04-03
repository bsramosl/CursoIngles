from django.contrib import admin

from .models import *


class ElegirRespuestaInline(admin.TabularInline):
	model = ChooseQuestionModel
	can_delete =False
	max_num = ChooseQuestionModel.MAXIMUN_RESPONSE
	min_num = ChooseQuestionModel.MAXIMUN_RESPONSE
 

class PreguntaAdmin(admin.ModelAdmin):
	model = QuestionModel
	inlines = (ElegirRespuestaInline, )
	list_display = ['texto',]
	search_fields = ['texto', 'preguntas__texto']